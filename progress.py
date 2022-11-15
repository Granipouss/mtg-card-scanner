import time
import math


def timeFormat(s):
    if s < 1:
      return "%.2fms" % (1000 * s)
    m = math.floor(s / 60)
    h = math.floor(m / 60)
    s = s - 60 * m
    m = m - 60 * h
    str = "%.2fs" % (s)
    if m > 0:
        str = "%im " % (m) + str
    if h > 0:
        str = "%ih " % (h) + str
    return str


class ProgressBar:
    width = 40
    renderDeltaTime = 1 / 24

    startTime = 0
    lastRenderTime = 0

    length = 10
    current = 0

    def __init__(self, length):
        self.length = max(1, int(length))
        self.current = 0
        self.startTime = time.time()

        self.render(True)

    def render(self, force=False):
        now = time.time()
        if (not force) and (now - self.lastRenderTime < self.renderDeltaTime):
            return
        self.lastRenderTime = now

        rate = self.current / self.length
        x = int(rate * self.width)
        totalTime = now - self.startTime
        averageTime = totalTime / max(1, self.current)
        estimatedTime = averageTime * (self.length - self.current)
        print("[%s%s] %i%% | tot %s | avg %s | est %s | %i/%i     " % ("=" * x, "-" * (self.width - x),
              100 * rate, timeFormat(totalTime), timeFormat(averageTime), timeFormat(estimatedTime), self.current, self.length), end="\r", flush=True)

    def tick(self):
        self.current = self.current + 1
        self.render()

    def stop(self):
        self.render(True)
        print("")
