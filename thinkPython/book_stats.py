from collections import defaultdict
import matplotlib.pyplot as plt
import string
import random


def process(f, skip_head = True):
    text = open(f, errors='ignore')
    if skip_head:
        skip_header(text)
    return text

def skip_header(text):
    for line in text:
        if '***' in line:
            break

def get_lines(text):
    tableWS = str.maketrans({key: None for key in string.whitespace[1:]})
    tableP = str.maketrans({key: None for key in string.punctuation})
    lines = [line.translate(tableWS) for line in text]
    lines = [line.translate(tableP).lower() for line in lines]
    lines = [line for line in lines if line != '']
    return lines

def get_words(lines):
    words = []
    for line in lines:
        words.extend(line.split(' '))
    words = [word for word in words if not has_number(word) and word!='']
    return words

def get_word_count(words):
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    return word_counts

def get_total_words(words):
    return len(words)

def unique_words(words, return_words = False):
    if return_words:
        return (len(set(words)), set(words))
    return len(set(words))

def inverse_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, key)
    return inverse


def top_twenty(word_counts):
    top_20 = []
    counts = inverse_dict(word_counts)
    top_20_vals = sorted(counts.keys(), reverse=True)[:21]
    for val in top_20_vals:
        top_20.append((counts[val], val))
    return top_20


def word_list():
    word_list = []
    fin = open('data/words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return sorted(word_list)


def has_number(word):
    if word.isdigit():
        return True
    nums = [str(x) for x in range(10)]
    for num in nums:
        if num in word:
            return True
    return False


def obscure_words(unqiue_words, word_list):
    obscure = []
    for word in unqiue_words:
        if len(word) <= 1 or has_number(word):
            pass
        elif word not in word_list:
            obscure.append(word)
    return obscure

def word_freqs(word_counts):
    words = []
    freqs = []
    total_freq = 0
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)
    return words, freq

def random_word(word_counts):
    words, freq = word_freqs(hist)
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]

def markov(words, prefix_length=2):
    markov_dict = defaultdict(list)
    for i in range(0, len(words)-(prefix_length+1)):
        markov_dict[words[i]+" "+words[i+(prefix_length-1)]].append(words[i+prefix_length])
    for pre, suf in markov_dict.items():
        markov_dict[pre] = list(set(suf))
    return markov_dict

def generate_text(words, prefix_length=2, num_chracters=1000):
    markov_dict = markov(words, prefix_length)
    text = ''
    prefix = random.choice(list(markov_dict.keys()))
    suffix = random.choice(markov_dict[prefix])
    text += (prefix+' '+suffix)
    while len(text) < num_chracters:
        prefix = prefix.split(" ")[1]+" "+suffix
        suffix = random.choice(markov_dict[prefix])
        text += (' '+suffix)
    return text

def zipfs_law(word_count):
    freqs = list(word_count.values())
    freqs.sort(reverse=True)
    rf = [((r+1),f) for r,f in enumerate(freqs)]
    return rf

def plot_ranks(word_count, scale='log'):
    """Plots frequency vs. rank.

    hist: map from word to frequency
    scale: string 'linear' or 'log'
    """
    rf = zipfs_law(word_count)
    rs, fs = zip(*rf)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()

def bookStats(book):
    text = process(book)
    lines = get_lines(text)
    words = get_words(lines)
    word_count = get_word_count(words)
    total = get_total_words(words)
    num_unique, unique = unique_words(words, return_words=True)
    top_20 = top_twenty(word_count)
    obscure = obscure_words(unique, word_list())
    stats_dict = {'lines': lines, 'words': words, 'word frequencies': word_count, 'total words':total,\
            'number of unique words': num_unique,'unique words': unique, \
                  '20 most common words': top_20, 'obscure words': obscure}
    return stats_dict
