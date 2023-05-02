# **Project 2: Truth Or Dare Box**
###### Blake Craig: Physical Computing -- No Utility

### What is the Truth Or Dare Box?
  The very fun and simple game that we all have played as kids, and even some now. Using a simple 3 button system, this game will allow you to explore many truths or dares of various ratings. The Truth Or Dare Box is adapted from the Discord [Truth Or Dare Bot](https://discord.gg/truth-or-dare-community-721108820339851285) and its [API](https://docs.truthordarebot.xyz/api-docs).

### Creator Statement:

### Resources Used:
1. Raspberry Pi 3
2. 3x Buttons
3. [2inch Waveshare LCD](https://www.amazon.com/2inch-IPS-LCD-Display-Module/dp/B082GFTZQD/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=WMFdL&content-id=amzn1.sym.1bcf206d-941a-4dd9-9560-bdaa3c824953&pf_rd_p=1bcf206d-941a-4dd9-9560-bdaa3c824953&pf_rd_r=KBBJ564QD1HR9P4DB2SV&pd_rd_wg=laHxs&pd_rd_r=6621cfda-114c-49d1-8ca7-f7b7649c0e4d&pd_rd_i=B082GFTZQD&th=1)
4. Wires for connection
5. Wooden Box for storage
6. Power Cord for Raspberry Pi 3 (5.1 V micro USB power supply)

### Rough Outline:
[Truth or Dare Pitch Slides](https://docs.google.com/presentation/d/1FzBwE5TaG55Q_4KGaa2dDfBRiit9njIaPZ8VvBIQmys/edit?usp=sharing)
   ![image](https://user-images.githubusercontent.com/112400887/235695310-5b562ccc-f879-402d-924a-b8895f6176c0.png)
  

### Code:
 Description: | Code: | Instruction:
 --- | --- | --- 
 This code is a good test that your LCD is working. I liked to edit the messages within the code to display and try the different shapes and designs. Fun to go on a creative hike through the different LCD Displays. | [Link to LCD Test](https://github.com/blakecraig25/Truth-or-Dare-Box/blob/main/2inch_LCD_test.py) | I plugged this into the raspberry pi using this [Waveshare Documentation](https://www.waveshare.com/wiki/2inch_LCD_Module) link. You will find some of the code commented out. This code still runs and can offer other options for your LCD. The bottomost code that is commented out shows a new image downloaded from the LCD Demo on Waveshare's. It isn't necessary for understanding how the LCD works, but could be useful for you. The font files were also downloaded from the demo as well. I made them available to this code by copying them from the demo into my Truth or Dare Box folder. Don't forget to import libraries.
 This code is good for makin sure that your API is running correctly. This code doesn't require and raspberry data, just simply your computer. | [Link to API Test](https://github.com/blakecraig25/Truth-or-Dare-Box/blob/main/ToD.py) | I had trouble with the VS Code Output, so I just used the terminal. It worked well. Follow the instructions of the code and feel free to edit.
 This code tests the API and the LCD. I would recommend testing the first two rows before testing this. I found that testing one part at a time was significantly faster. | [Link to Truth Or Dare Game: No Button](https://github.com/blakecraig25/Truth-or-Dare-Box/blob/main/ToD_LCDOnly.py) | This code is just like the instruction for the API. You can follow the instructions from the terminal and hopefully it displays the LCD responses. The questions may go out the right end of the LCD. Don't worry, I didn't implement a code to keep the entire question within the LCD screen. It is just a test. Feel free to copy the code from the complete code if you want to run LCD only.
 This is the entire code for the complete system. This code utilizes buttons. | [Link to Truth Or Dare Game: With Buttons](https://github.com/blakecraig25/Truth-or-Dare-Box/blob/main/truthordare.py) | This code will allow the user to press button 1, 2, or 3. Be careful, there are specific GPIO Pins using the BCM layout. These buttons are just attached to the GPIOs and ground, no need for a breadboard. I am using the internal resistors of the Raspberry Pi 3 instead of applying them myself. The output should result in screen changes to the next question. Test to make sure it does that. In addition, the terminal will display the values pressed and the question itself, in the event the LCD becomes disconnected. Refer to that to confim what users may have guessed.
 
### Useful Links for this project:
- [DevLogs](https://docs.google.com/document/d/1LjeJ5W5CIBxbFlulhDBlaNdNTP2VWx7RZiV6apDHc5M/edit?usp=sharing)
- [GitHub TruthorDare Repo](https://github.com/blakecraig25/Truth-or-Dare-Box)
- [Waveshare Documentation](https://www.waveshare.com/wiki/2inch_LCD_Module)
- []()

### Similar Projects:
- [You Have Been Blinded and Thrown in a Dungeon](https://www.jeffreythompson.org/projects/you-have-been-blinded-and-thrown-in-a-dungeon.php)
- [Mini Arcade Machine](https://github.com/obernardovieira/Mini-Arcade-Machine)
