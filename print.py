import json

def main():
    with open("pose-json/base-poses.json", 'r') as file:
        yeet = json.loads(file.readline())
        print(json.dumps(yeet, indent=4))


if __name__ == "__main__":
    main()