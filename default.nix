with import <nixpkgs> {}; {
  pyEnv = stdenv.mkDerivation {
    name = "nix-shell";
    buildInputs = [ stdenv alsaLib ];
    shellHook = ''
      unset http_proxy
      export LIBRARY_PATH=${pkgs.alsaLib.out}/lib
    '';
  };
}
