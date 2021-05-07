
class Logger:
    def log(self, header, message):
        with open('logfile', 'a+') as writer:
            writer.write("[{}] {}".format(header, message)+"\n")
    