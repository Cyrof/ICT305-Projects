{
  pkgs,
  ...
}:

{
  languages.python = {
    enable = true;
    uv.enable = true;
  };

  # Native dependency for NumPy.
  env = {
    LD_LIBRARY_PATH = "${pkgs.lib.makeLibraryPath (with pkgs; [ libz ])}:$LD_LIBRARY_PATH";
  };
}
