#!/usr/bin/env python3
import os
import sys
programPath = os.path.split(os.path.realpath(__file__))[0] 
os.system(f"bash '{programPath}/incremental-updating-packages.sh' '{programPath}'")
os.system("apt-ftparchive release . > Release")
os.system("rm Release.gpg")
os.system("rm InRelease")
os.system("rm gpg.asc")
#os.system("gpg --armor --detach-sign -o Release.gpg Release")
#os.system("gpg --clearsign -o InRelease Release")
#os.system("gpg --passphrase=\"$KEYPASSWORD\" --armor --output gpg.asc --export 3025613752@qq.com ")
os.system('gpg --default-key "3025613752@qq.com" --batch --pinentry-mode="loopback" --passphrase="$KEYPASSWORD" -abs -o - Release > Release.gpg || error "failed to sign Release.gpg with gpg "')
os.system('gpg --default-key "3025613752@qq.com" --batch --pinentry-mode="loopback" --passphrase="$KEYPASSWORD" --clearsign -o - Release > InRelease || error "failed to sign InRelease with gpg"')