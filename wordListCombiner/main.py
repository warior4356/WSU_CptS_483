import time

def main():
    start_time = time.time()
    words = []
    wordfile = open('./wordlist.10000.txt', 'r')
    outfile = open('./outfile.txt', 'w')

    for word in wordfile:
        words.append(word.strip())

    for word1 in words:
        for word2 in words:
            outfile.write('{}{}\n'.format(word1, word2))

    end_time = time.time()
    elapsed = end_time - start_time
    print('Elapsed time program was {} seconds'.format(elapsed))

if __name__ == "__main__":
  main()