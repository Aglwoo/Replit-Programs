// Constants
const SENSITIVITY = 0.5, // How sensitive the game is to output
  POPSIZE = 200 // Population size
  MUTATION_RATE = 10,
  MUTATION_AMOUNT = 100

let EXTREME = false

kaboom({
  background: [135, 206, 235]
});

loadBean()

add([
  pos(0, 80),
  rect(2000, 1000),
  outline(4),
  area(),
  solid()
])

for(let i = 0; i < 10; i++){
  for(let e = 0; e < 10; e++){
    let y = ((-1000 * i) + (e * 150))
    if(y > 0) continue;
    
    add([
      pos(e * 100, y),
      rect(100, 10),
      outline(4),
      area(),
      solid()
    ])
  }
}

let txt = {
  generation: add([
    text("Generation 0", {size: 50}),
    pos(50, 50),
    fixed()
  ]),
  deaths: add([
    text("No deaths", {size: 50}),
    pos(50, 100),
    fixed()
  ]),
  time: add([
    text("Time: 1", {size: 50}),
    pos(50, 150),
    fixed()
  ]),
  extreme: add([
    text("", {size: 50}),
    pos(50, 200),
    fixed(),
    color(200, 0, 0)
  ])
}

camPos(500,0)
camScale(0.5)

let players = []
let evaluationTimer = setTimeout(()=>{},0)

let camTo = vec2(500,0)

function Player(g, i){
  let thisReally = this

  this.brain = g;
  this.brain.score = 0;
  
  this.me = add([
    sprite("bean"),
    pos((60 * i) + 200, 20),
    area(),
    body(),
    outview({ 
      delay: 1
    }),
    "player"
  ])

  setTimeout(()=>{
    this.me.on(`exitView`, ()=>{
      if(!this.me.pos.y < 0) return;
      
      this.brain.score = 0
      this.me.destroy()
      players = players.filter(function(item) {
        return item !== thisReally
      })
      if(players.length === 0) {
        clearTimeout(evaluationTimer)
        endEvaluation()
      }

      txt.deaths.text = `${POPSIZE - players.length} Deaths`
    })
  },250)

  this.update = ()=>{
    let d = this.brain.activate([(100 - this.me.pos.x) / 1000, this.me.pos.y / 1000]) // Make a decision

    if(d[0] > SENSITIVITY){
      this.me.moveBy(EXTREME ? 20 : 10, 0)
    }
    if(d[1] > SENSITIVITY){
      this.me.moveBy(EXTREME ? -20 : -10, 0)
    }
    if(d[2] > SENSITIVITY && this.me.isGrounded()){
      this.me.jump(EXTREME ? 1500 : 1000)
    }

    if(this.me.pos.y / 100 > this.brain.score){
      this.brain.score = this.me.pos.y / 100
    }

    // camera
    let special = true
    
    for(let i=0; i<players.length; i++){
      if(players[i].pos == this.me.pos) continue;
      
      if(players[i].me.pos.y < this.me.pos.y){
        special = false
        break;
      }
    }

    if(special){
      camTo = this.me.pos
    }
  }

  players.push(this)
}

const neat = new neataptic.Neat(2, 3, null, {
    popsize: POPSIZE,
    elitism: 0,
    mutationRate: MUTATION_RATE,
    mutationAmount: MUTATION_AMOUNT
  }
)

function startEvaluation(){
  players = [];
  highestScore = 0;

  let i = 0;

  for(let genome in neat.population){
    genome = neat.population[genome];
    new Player(genome, i);
    i++
  }

  let time = ((neat.generation * 100) + 1000)

  if(EXTREME) time = time / 1.5

  time = Number(time.toFixed(1))

  evaluationTimer = setTimeout(()=>{
    endEvaluation()
  },time)

  txt.deaths.text = `No deaths`
  txt.generation.text = `Generation ${neat.generation}`
  txt.time.text = `Time: ${(time) / 1000}`
}

function endEvaluation(){
  console.log('Generation:', neat.generation, '- average score:', neat.getAverage());

  neat.sort();
  let newPopulation = [];

  // Order self-destruct
  destroyAll("player")
  players = []

  // Elitism
  for(let i = 0; i < neat.elitism; i++){
    newPopulation.push(neat.population[i]);
  }

  // Breed the next individuals
  for(let i = 0; i < neat.popsize - neat.elitism; i++){
    newPopulation.push(neat.getOffspring());
  }

  // Replace the old population with the new population
  neat.population = newPopulation;
  neat.mutate();

  neat.generation++;
  startEvaluation();
}

startEvaluation()

onUpdate(()=>{
  for(let i=0; i<players.length; i++){
    players[i].update();
  }

  let cam = camPos()
  if(camTo.x > cam.x){
    cam.x++
  }else if(camTo.x < cam.x){
    cam.x--
  }

  if(camTo.y > cam.y){
    cam.y++
  }else if(camTo.y < cam.y){
    cam.y--
  }

  camPos(cam)
})

onKeyPress("e", () => {
  EXTREME = EXTREME ? false : true

  if(EXTREME){
    txt.extreme.text = `Extreme/Fast`
  }else{
    txt.extreme.text = ``
  }
})