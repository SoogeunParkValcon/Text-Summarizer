import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        """
        This class is used to execute data validation
        """
        self.config = config
        
        # also I initialize the tokenizer - adopted from the information given in the config.yaml
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
    
    # now I need the function that convert data ('examples') into features ('tokens')
    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], 
                                         max_length = 1024,
                                         truncation = True)
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'],
                                              max_length = 128,
                                              truncation = True)
            
        return{
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    # this method then executes the data transformation
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        logger.info(f"Dataset loaded from {self.config.data_path}.")
        
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        # batched processing instead of individual observation unit processing, to allow more efficient processing
        
        logger.info(f"Dataset converted to features successfully.")
        
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, self.config.result_file_name))
        
        logger.info(f"Dataset saved at {os.path.join(self.config.root_dir, self.config.result_file_name)}.")