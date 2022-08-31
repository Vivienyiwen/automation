# automation

### Note: make sure you already login to WhatsApp web in your chrome browser

1.Send a message to someone on WhatsApp:

```ruby
import pywhatkit
pywhatkit.sendwhatmsg("+65*****","message",13,23)
```
In 38 Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!

2. Send a message to a group on WhatsApp:

```ruby
import pywhatkit
#syntax: group link, message, hour and minutes
pywhatkit.sendwhatmsg_to_group("group-link", "Your Message", 12, 01)
```


