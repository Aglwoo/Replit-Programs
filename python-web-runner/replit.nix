{ pkgs }: {
  deps = [
    pkgs.replitPackages.prybar-python3
    pkgs.chromium
    pkgs.chromedriver
  ];
}