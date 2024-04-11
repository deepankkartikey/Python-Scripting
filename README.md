This repository consists of multiple small python automation scripts that I created while learning Python!

### Getting Started
- Install (latest) Python version
- Install virtual environment utility
   ```
   pip3 install virtualenv
   ```
- Create a virtual environment
   ```
   virtualenv <environment_name>
   ```
- Run the following command in the parent directory to install Python dependecies needed to run the scripts:
   ```
   pip3 install -r requirements.txt
   ```

#### List of Scripts available
- **[Downloads Sorter](./Automated-Downloads-Sorter/)**
   - Automatically sorts downloaded files into music, video, image, pdf documents, code files, etc.
- **[Youtube Video Downloader](./Youtube-Downloader/)**
   - Downloads either a youtube video or a playlist based on type of URL that is passed as script parameter while running it.
- **[PDF-Merger](./PDF-Merger/)**
   - Merge two or more PDF files into one.
   - When script is run, all pdf files in current directory are combined and a new combined file is generated.
- **[Price-Tracker](./eBay-Price-Tracker/)**
   - Get current price of an eBay product by giving the eBay product URL as user input
   - Currently, supports only eBay - more website supports will be added in future
