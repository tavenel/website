{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  # https://devenv.sh/basics/
  env.ASTRO_TELEMETRY_DISABLED = "1";

  # https://devenv.sh/packages/
  packages = with pkgs; [
		git
		bun
	];

  # https://devenv.sh/languages/
  languages.typescript.enable = true;

  # https://devenv.sh/processes/
  # processes.dev.exec = "${lib.getExe pkgs.watchexec} -n -- ls -la";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/
	scripts = {
		dev = {
			exec = "bun run dev";
			description = "Start Astro development server";
		};

		build = {
			exec = "bun run build";
			description = "Build Astro for production";
		};

		preview = {
			exec = "bun run preview";
			description = "Preview production build";
		};

		check = {
			exec = "bun run check";
			description = "Run Astro checks";
		};

    upgrade = {
			exec = "${pkgs.bun}/bin/bun x @astrojs/upgrade";
			description = "Upgrade Astro using bun x";
		};

	};


  # https://devenv.sh/basics/
  enterShell = ''
    echo "🚀 Astro development environment"
    echo "Bun $(bun --version)"
  '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/git-hooks/
  # git-hooks.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
