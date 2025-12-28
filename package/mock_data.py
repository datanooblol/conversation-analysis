import pandas as pd

conversations = [
    # Session 1: Convert - Product inquiry to purchase
    ('s1', 1, 'Hi, I need help choosing a laptop', 'I can help you find the perfect laptop. What will you use it for?', 'inquiry', 'convert', '2024-06-01 10:00:00'),
    ('s1', 2, 'Gaming and video editing', 'For gaming and video editing, I recommend our high-performance models with dedicated graphics.', 'specification', 'convert', '2024-06-01 10:15:00'),
    ('s1', 3, 'What about the price range?', 'Our gaming laptops range from $1200-$3000. What is your budget?', 'pricing', 'convert', '2024-06-01 10:30:00'),
    ('s1', 4, 'Around $2000 sounds good', 'Perfect! I have a great model at $1899 that fits your needs. Shall I add it to your cart?', 'purchase_intent', 'convert', '2024-06-01 10:45:00'),
    ('s1', 5, 'Yes, please proceed', 'Great! I have added the laptop to your cart. Proceeding to checkout.', 'purchase', 'convert', '2024-06-01 11:00:00'),
    
    # Session 2: Bounce - Quick exit
    ('s2', 1, 'Do you have refurbished phones?', 'Yes, we have certified refurbished phones with warranty. Would you like to see our selection?', 'inquiry', 'bounce', '2024-06-02 09:00:00'),
    ('s2', 2, 'Never mind, thanks', 'No problem! Feel free to reach out if you change your mind.', 'exit', 'bounce', '2024-06-02 09:02:00'),
    
    # Session 3: Convert - Support to upsell
    ('s3', 1, 'My order is delayed, when will it arrive?', 'Let me check your order status. Can you provide your order number?', 'support', 'convert', '2024-06-03 14:00:00'),
    ('s3', 2, 'Order #12345', 'Your order will arrive tomorrow. While I have you, would you be interested in our premium support plan?', 'upsell', 'convert', '2024-06-03 14:05:00'),
    ('s3', 3, 'What does it include?', 'Premium support includes 24/7 chat, priority shipping, and extended warranty for just $99/year.', 'specification', 'convert', '2024-06-03 14:10:00'),
    ('s3', 4, 'Sounds good, sign me up', 'Excellent! I have added premium support to your account. You are all set!', 'purchase', 'convert', '2024-06-03 14:15:00'),
    
    # Session 4: Bounce - Price objection
    ('s4', 1, 'I want to buy a tablet for my kids', 'Great choice! Our kid-friendly tablets have parental controls and educational apps. Which age group?', 'inquiry', 'bounce', '2024-06-04 16:00:00'),
    ('s4', 2, '8-10 years old', 'Perfect! Our KidTab Pro is ideal for that age. It is $299 with a protective case included.', 'specification', 'bounce', '2024-06-04 16:05:00'),
    ('s4', 3, 'That is too expensive for me', 'I understand. We also have a basic model for $149. Would that work better?', 'pricing', 'bounce', '2024-06-04 16:10:00'),
    ('s4', 4, 'Still too much, thanks anyway', 'No worries! Keep an eye out for our seasonal sales. Have a great day!', 'exit', 'bounce', '2024-06-04 16:12:00'),
    
    # Session 5: Convert - Information to purchase
    ('s5', 1, 'What are your store hours?', 'Our stores are open Monday-Saturday 9AM-9PM, Sunday 11AM-7PM. Can I help you with anything else?', 'information', 'convert', '2024-06-05 12:00:00'),
    ('s5', 2, 'Do you have wireless earbuds in stock?', 'Yes! We have several models available. Are you looking for any specific brand or features?', 'inquiry', 'convert', '2024-06-05 12:05:00'),
    ('s5', 3, 'Something with good battery life', 'Our PowerBuds have 30-hour battery life and excellent sound quality for $179. Very popular!', 'specification', 'convert', '2024-06-05 12:10:00'),
    ('s5', 4, 'Can I pick them up today?', 'Absolutely! I can reserve them for pickup. What is your name and preferred pickup time?', 'purchase_intent', 'convert', '2024-06-05 12:15:00'),
    ('s5', 5, 'John Smith, around 3PM', 'Perfect! Reserved PowerBuds for John Smith, pickup by 3PM today. See you then!', 'purchase', 'convert', '2024-06-05 12:20:00'),
    
    # Session 6: Bounce - Comparison shopping
    ('s6', 1, 'How much is the iPhone 15?', 'The iPhone 15 starts at $799 for 128GB. We also have financing options available.', 'pricing', 'bounce', '2024-06-06 10:30:00'),
    ('s6', 2, 'What about trade-in value for iPhone 12?', 'iPhone 12 trade-in value is up to $400 depending on condition. Would you like a quote?', 'trade_in', 'bounce', '2024-06-06 10:35:00'),
    ('s6', 3, 'I will think about it and compare prices', 'Of course! Take your time. Our prices are competitive and we price match. Let me know if you have questions!', 'exit', 'bounce', '2024-06-06 10:40:00'),
    
    # Session 7: Bounce - Repeated inquiries without progress
    ('s7', 1, 'Do you sell smart watches?', 'Yes, we have a wide selection of smart watches. What features are you looking for?', 'inquiry', 'bounce', '2024-06-07 15:00:00'),
    ('s7', 2, 'What brands do you carry?', 'We carry Apple Watch, Samsung Galaxy Watch, Fitbit, and Garmin. Any preference?', 'inquiry', 'bounce', '2024-06-07 15:05:00'),
    ('s7', 3, 'What about fitness tracking?', 'All our smart watches have fitness tracking. Some have advanced health monitoring too. Which activities do you track?', 'inquiry', 'bounce', '2024-06-07 15:10:00'),
    ('s7', 4, 'Thanks, I need to research more', 'No problem! Feel free to come back when you are ready. Have a great day!', 'exit', 'bounce', '2024-06-07 15:12:00')
]

df = pd.DataFrame(conversations, columns=['session_id', 'turn', 'user_message', 'assistant_message', 'state', 'outcome', 'timestamp'])
df['timestamp'] = pd.to_datetime(df['timestamp'])