from itemadapter import ItemAdapter
import json

class LivemintScrapperPipeline:
    def open_spider(self, spider):
        self.file = open('articles.json', 'a')
        self.json_list = []

    def close_spider(self, spider):
        # Serialize the list of dictionaries to JSON string with indentation for readability
        json_data = json.dumps(self.json_list, indent=4)
        
        # Write the JSON data to the file
        self.file.write(json_data)
        self.file.close()

    def process_item(self, item, spider):
        # Convert the LivemintScraperItem object to a dictionary
        item_dict = dict(item)
        
        # Append the dictionary to the list
        self.json_list.append(item_dict)
        
        return item
