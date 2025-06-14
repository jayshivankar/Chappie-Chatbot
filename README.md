# 🤖 Chappie Chatbot – AI-Powered Assistant for Food Ordering

**Chappie** is an intelligent chatbot assistant built using **FastAPI** and **Dialogflow**, integrated into a food ordering web app — **StreetCrave Pune**. It allows users to place orders, check prices, and track food deliveries via natural conversation.

---

## 🚀 Features

- 🍽️ Add food items with specific quantities via chat  
- 📦 Track real-time order status using order ID  
- 🧾 Calculate and return total price of current order  
- 📋 Dialogflow-integrated conversational interface  
- 🧠 Stores all orders using a MySQL backend with stored procedures

---

## 🧠 How It Works

### 🔹 Dialogflow Webhook Flow
1. User interacts with Dialogflow Messenger on the website.
2. Requests are routed to FastAPI backend (`main.py`).
3. Based on intent, relevant handler functions are called:
   - `order-add`
   - `order-complete`
   - `track-order`

### 🔹 Order Management
- Session tracking is done via extracted session IDs.
- Items added are stored in memory (`inprogress_orders`) until confirmed.
- Orders are inserted into a MySQL database and tracked via custom SQL procedures.

---

## 🛠 Tech Stack

| Component     | Tech/Tool                     |
|---------------|-------------------------------|
| UI            | HTML, CSS, Dialogflow Messenger |
| Backend       | FastAPI (Python)              |
| DB            | MySQL + Stored Procedures     |
| Utilities     | Pandas, Regex, LangDetect     |
| Logic         | Dialogflow CX Intents         |

---

## 📁 Project Structure

```
.
├── main.py            # FastAPI server + intent handlers
├── db_helper.py       # MySQL database logic
├── helper_file.py     # Utility functions (session parsing, dict formatting)
├── index.html         # Frontend (StreetCrave menu + Dialogflow)
├── schema.sql         # MySQL table & stored procedures
```

---

## 💬 Core Functionalities

### ✅ Add to Order
Users can say things like:
```
I'd like 2 Samosas and 1 Pav Bhaji
```

### ✅ Complete Order
Once ready, users confirm the order and get:
- Order ID
- Total Price

### ✅ Track Order
Say:
```
Track my order #4
```
Chappie replies with the current status from the database.

---

## 🧪 Sample Dialogflow Integration (HTML)

```html
<df-messenger
  intent="WELCOME"
  chat-title="Chappie Chatbot"
  agent-id="YOUR_AGENT_ID"
  language-code="en"
></df-messenger>
```

---

## 💾 MySQL Stored Procedures (schema.sql)

```sql
CREATE PROCEDURE insert_order_item(IN food_item VARCHAR(100), IN quantity INT, IN order_id INT)
BEGIN
  INSERT INTO order_items (order_id, item_name, quantity)
  VALUES (order_id, food_item, quantity);
END;

CREATE FUNCTION get_total_order_price(order_id INT)
RETURNS DECIMAL(10,2)
BEGIN
  DECLARE total_price DECIMAL(10,2);
  SELECT SUM(quantity * price)
  INTO total_price
  FROM order_items JOIN menu ON item_name = menu.name
  WHERE order_id = order_items.order_id;
  RETURN total_price;
END;
```

---

## 📸 UI Preview

> Food Ordering Site + Chatbot (StreetCrave Pune)

![food-chatbot_1](https://github.com/user-attachments/assets/c8c71fd2-3889-4633-8896-d8466c102c63)

---

## 📌 Prerequisites

- Python 3.8+
- MySQL Server
- FastAPI: `pip install fastapi uvicorn mysql-connector-python`
- Dialogflow Agent ID (CX or ES)

---

## 🚀 How to Run

1. Clone this repo
2. Run your MySQL server and create the `pandeyji_eatery` DB using `schema.sql`
3. Run backend:
   ```
   uvicorn main:app --reload
   ```
4. Open `index.html` in browser
5. Start chatting with Chappie!

---

## 🙌 Contributions

Pull requests and feedback welcome!

---

## 📬 Contact

Made with ❤️ by [Your Name]  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | 🧠 [GitHub](https://github.com/yourusername)

