;;; Directory Local Variables  -*- no-byte-compile: t -*-
((nil . ((eval . (setenv "PUPPETEER_EXECUTABLE_PATH"
                         "/home/mic/.cache/puppeteer/chrome-headless-shell/linux-148.0.7778.167/chrome-headless-shell-linux64/chrome-headless-shell"))
         (dape-command . (debugpy
                          modes (python-mode python-ts-mode)
                          command (expand-file-name
                                   ".venv/bin/python"
                                   (locate-dominating-file
                                    default-directory ".venv"))
                          command-args ("-m" "debugpy.adapter" "--host" "127.0.0.1" "--port" :autoport)
                          port :autoport
                          :type "python"
                          :request "launch"
                          :program dape-buffer-default
                          :cwd dape-cwd
                          :console "internalConsole"
                          :justMyCode t)))))
