import os


base_path = "/home/yihan.wang/project/mk_sql/data/yelp-gpt2-control-only"
max_source_length = 512
max_decoding_length = 5

source_vocab_file = os.path.join(base_path, "vocab.source.negative")
target_vocab_file = os.path.join(base_path, "vocab.target")

train = {
    "batch_size": 12,
    "allow_smaller_final_batch": False,
    "shuffle": False,
    "source_dataset": {
        "files": os.path.join(base_path, "train.source.negative"),
        "vocab_file": source_vocab_file,
    },
    "target_dataset": {
        "files": os.path.join(base_path, "train.target.negative"),
        "vocab_file": target_vocab_file,
    }
}

# No Validation and Test
val = {
    "batch_size": 10,
    "shuffle": False,
    "source_dataset": {
        "files": os.path.join(base_path, "dev.source.negative"),
        "vocab_file": source_vocab_file,
    },
    "target_dataset": {
        "files": os.path.join(base_path, "dev.target.negative"),
        "vocab_file": target_vocab_file,
    }
}

# No Validation and Test
test = {
    "batch_size": 10,
    "shuffle": False,
    "source_dataset": {
        "files": os.path.join(base_path, "dev.source.negative"),
        "vocab_file": source_vocab_file,
    },
    "target_dataset": {
        "files": os.path.join(base_path, "dev.target.negative"),
        "vocab_file": target_vocab_file,
    }
}
