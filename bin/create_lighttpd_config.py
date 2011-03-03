#!/usr/bin/env python
import os.path

baseDir = os.path.abspath(".")

configFileName = "lighttpd_this_dir.conf"
configFileAbs = "%s/%s" % (baseDir, configFileName)
configFile = open(configFileAbs, "w")

contents = []
contents.append("server.document-root = \"%s\"" % (baseDir) )
contents.append("server.port = 6789")
contents.append('# mimetype mapping')
contents.append('mimetype.assign            = (')
contents.append('  ".pdf"          =>      "application/pdf",')
contents.append('  ".sig"          =>      "application/pgp-signature",')
contents.append('  ".spl"          =>      "application/futuresplash",')
contents.append('  ".class"        =>      "application/octet-stream",')
contents.append('  ".ps"           =>      "application/postscript",')
contents.append('  ".torrent"      =>      "application/x-bittorrent",')
contents.append('  ".dvi"          =>      "application/x-dvi",')
contents.append('  ".gz"           =>      "application/x-gzip",')
contents.append('  ".pac"          =>      "application/x-ns-proxy-autoconfig",')
contents.append('  ".swf"          =>      "application/x-shockwave-flash",')
contents.append('  ".tar.gz"       =>      "application/x-tgz",')
contents.append('  ".tgz"          =>      "application/x-tgz",')
contents.append('  ".tar"          =>      "application/x-tar",')
contents.append('  ".zip"          =>      "application/zip",')
contents.append('  ".mp3"          =>      "audio/mpeg",')
contents.append('  ".m3u"          =>      "audio/x-mpegurl",')
contents.append('  ".wma"          =>      "audio/x-ms-wma",')
contents.append('  ".wax"          =>      "audio/x-ms-wax",')
contents.append('  ".ogg"          =>      "audio/x-wav",')
contents.append('  ".wav"          =>      "audio/x-wav",')
contents.append('  ".gif"          =>      "image/gif",')
contents.append('  ".jpg"          =>      "image/jpeg",')
contents.append('  ".jpeg"         =>      "image/jpeg",')
contents.append('  ".png"          =>      "image/png",')
contents.append('  ".xbm"          =>      "image/x-xbitmap",')
contents.append('  ".xpm"          =>      "image/x-xpixmap",')
contents.append('  ".xwd"          =>      "image/x-xwindowdump",')
contents.append('  ".css"          =>      "text/css",')
contents.append('  ".html"         =>      "text/html",')
contents.append('  ".htm"          =>      "text/html",')
contents.append('  ".js"           =>      "text/javascript",')
contents.append('  ".asc"          =>      "text/plain",')
contents.append('  ".c"            =>      "text/plain",')
contents.append('  ".conf"         =>      "text/plain",')
contents.append('  ".text"         =>      "text/plain",')
contents.append('  ".txt"          =>      "text/plain",')
contents.append('  ".dtd"          =>      "text/xml",')
contents.append('  ".xml"          =>      "text/xml",')
contents.append( ')')

for line in contents:
    configFile.write(line)
    configFile.write("\n")
configFile.close()

import subprocess
import sys

cmd = ['lighttpd', '-D', '-f', configFileName]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
try:
    print "PID: %s" % (p.pid)
    for line in p.stdout:
        print line
    p.wait()
except KeyboardInterrupt:
    for line in p.stdout:
        print line


