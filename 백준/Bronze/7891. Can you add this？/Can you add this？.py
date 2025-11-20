import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    out_lines = []
    idx = 1
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        out_lines.append(str(x + y))
        idx += 2
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
