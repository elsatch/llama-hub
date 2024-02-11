# ArchiveBox Loader

This loader loads documents from an archivebox directory. When using the recommended official Docker Compose image, the files are located under the data folder, at the same level as the docker-compose.yml file.

## Usage

Here's an example usage of the ArchiveboxReader.

```python
from llama_index import download_loader
import os

ArchiveboxReader = download_loader('ArchiveboxReader')
documents = ArchiveboxReader('/path/to/data/dir').load_data() # Returns list of documents
```

This loader is designed to be used as a way to load data into [LlamaIndex](https://github.com/run-llama/llama_index/tree/main/llama_index) and/or subsequently used as a Tool in a [LangChain](https://github.com/hwchase17/langchain) Agent. See [here](https://github.com/emptycrown/llama-hub/tree/main) for examples.
