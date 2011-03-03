#!/usr/bin/env python
import os, os.path, sys
import subprocess

def create_config_file(absPath, port=6789):
    configFileName = "lighttpd_this_dir.conf"
    configFileAbs = "%s/%s" % (absPath, configFileName)
    configFile = open(configFileAbs, "w")

    contents = []
    contents.append("server.document-root = \"%s\"" % (absPath) )
    contents.append("server.port = %s" % (port))

    contents.append('# mimetype mapping')
    contents.append('mimetype.assign            = (')
    contents.append('  ".pdf"          =>      "application/pdf",')
    contents.append('  ".swf"          =>      "application/x-shockwave-flash",')
    contents.append('  ".gif"          =>      "image/gif",')
    contents.append('  ".jpg"          =>      "image/jpeg",')
    contents.append('  ".jpeg"         =>      "image/jpeg",')
    contents.append('  ".png"          =>      "image/png",')
    contents.append('  ".css"          =>      "text/css",')
    contents.append('  ".html"         =>      "text/html",')
    contents.append('  ".htm"          =>      "text/html",')
    contents.append('  ".js"           =>      "text/javascript",')
    contents.append('  ".conf"         =>      "text/plain",')
    contents.append('  ".txt"          =>      "text/plain",')
    contents.append('  ".xml"          =>      "text/xml",')
    contents.append( ')')

    for line in contents:
        configFile.write(line)
        configFile.write("\n")
    configFile.close()

    return configFileName


def start_server(configFileName):
    cmd = ['lighttpd', '-D', '-f', configFileName]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    try:
        for line in p.stdout: print line
        p.wait()
    except KeyboardInterrupt:
        for line in p.stdout: print line
        p.wait()

def remove_config_file(absFileName):
    os.remove(absFileName)

if __name__ == "__main__":
    port = 6789
    if len(sys.argv) > 1: port = sys.argv[1]

    absPath = os.path.abspath(".")
    fileName = create_config_file(absPath, port)
    start_server(fileName)
    remove_config_file("%s/%s" % (absPath, fileName))
