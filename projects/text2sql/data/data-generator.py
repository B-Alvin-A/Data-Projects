import random
from faker import Faker

# --- SEED FOR REPRODUCIBILITY ---
random.seed(42)
Faker.seed(42)
fake = Faker('en_GB')

# --- CONFIGURATION ---
NUM_CUSTOMERS = 200
NUM_ORDERS = 300

ugandan_products = [
    # Groceries
    ('Super Rice 5kg', 'Groceries', 28000), ('Super Rice 10kg', 'Groceries', 52000),
    ('Cooking Oil 3L', 'Groceries', 21000), ('Cooking Oil 5L', 'Groceries', 35000),
    ('Organic Coffee 500g', 'Groceries', 15000), ('Organic Coffee 250g', 'Groceries', 8500),
    ('Instant Coffee Bag', 'Groceries', 12000), ('Instant Coffee Jar', 'Groceries', 25000),
    ('Maize Flour 10kg', 'Groceries', 32000), ('Maize Flour 5kg', 'Groceries', 17000),
    ('Sugar 2kg', 'Groceries', 10000), ('Sugar 5kg', 'Groceries', 24000),
    ('Beans 2kg', 'Groceries', 12000), ('Beans 5kg', 'Groceries', 28000),
    ('Posho Flour 2kg', 'Groceries', 6000), ('Posho Flour 5kg', 'Groceries', 14000),
    ('Groundnuts 1kg', 'Groceries', 15000), ('Groundnuts 500g', 'Groceries', 8000),
    ('Salt 1kg', 'Groceries', 3000), ('Salt 500g', 'Groceries', 1800),
    ('Tea Leaves 500g', 'Groceries', 7000), ('Tea Bags 100ct', 'Groceries', 9000),
    ('Milk Powder 1kg', 'Groceries', 25000), ('Milk Powder 500g', 'Groceries', 13000),
    ('Tomato Paste 500g', 'Groceries', 5000), ('Tomato Sauce 1L', 'Groceries', 8000),
    ('Spaghetti 500g', 'Groceries', 4000), ('Spaghetti 1kg', 'Groceries', 7500),
    ('Cooking Gas 6kg', 'Groceries', 85000), ('Cooking Gas 12kg', 'Groceries', 160000),
    ('Mineral Water 500ml', 'Groceries', 1500), ('Mineral Water 1.5L', 'Groceries', 3000),
    ('Soda Assorted', 'Groceries', 2500), ('Beer Local', 'Groceries', 4000),
    
    # Electronics
    ('Solar Lantern', 'Electronics', 55000), ('Solar Panel 50W', 'Electronics', 120000),
    ('Solar Panel 100W', 'Electronics', 220000), ('Solar Battery 12V', 'Electronics', 280000),
    ('Power Bank 10k mAh', 'Electronics', 75000), ('Power Bank 20k mAh', 'Electronics', 120000),
    ('Electric Kettle', 'Electronics', 65000), ('Electric Iron', 'Electronics', 70000),
    ('Blender', 'Electronics', 95000), ('Microwave Oven', 'Electronics', 320000),
    ('TV 24 inch', 'Electronics', 380000), ('TV 32 inch', 'Electronics', 520000),
    ('Radio FM', 'Electronics', 45000), ('Boombox Bluetooth', 'Electronics', 110000),
    ('Headphones Wireless', 'Electronics', 35000), ('Earphones', 'Electronics', 15000),
    ('Phone Charger', 'Electronics', 12000), ('Phone Cable', 'Electronics', 5000),
    ('Memory Card 32GB', 'Electronics', 25000), ('Memory Card 64GB', 'Electronics', 45000),
    ('Flashlight Rechargeable', 'Electronics', 18000), ('Emergency Lamp', 'Electronics', 25000),
    ('Electric Cooker', 'Electronics', 185000), ('Frying Pan Electric', 'Electronics', 75000),
    
    # Clothing
    ('Leather Sandals', 'Clothing', 40000), ('Men\'s Shoes', 'Clothing', 85000),
    ('Women\'s Shoes', 'Clothing', 75000), ('School Shoes', 'Clothing', 45000),
    ('Men\'s Shirt', 'Clothing', 35000), ('Men\'s Trousers', 'Clothing', 45000),
    ('Women\'s Dress', 'Clothing', 55000), ('Women\'s Skirt', 'Clothing', 35000),
    ('Kids T-Shirt', 'Clothing', 15000), ('Kids Shorts', 'Clothing', 12000),
    ('School Uniform Shirt', 'Clothing', 25000), ('School Uniform Shorts', 'Clothing', 20000),
    ('Sweater', 'Clothing', 45000), ('Jacket', 'Clothing', 75000),
    ('Gomesi', 'Clothing', 120000), ('Kanzu', 'Clothing', 85000),
    ('Sportswear Set', 'Clothing', 65000), ('Running Shoes', 'Clothing', 95000),
    ('Flip Flops', 'Clothing', 8000), ('Socks 3 Pack', 'Clothing', 5000),
    ('Underwear 2 Pack', 'Clothing', 10000), ('Cap', 'Clothing', 12000),
    
    # Home & Garden
    ('Plastic Chair', 'Home & Garden', 25000), ('Wooden Chair', 'Home & Garden', 65000),
    ('Plastic Table', 'Home & Garden', 45000), ('Wooden Table', 'Home & Garden', 120000),
    ('Mosquito Net', 'Home & Garden', 18000), ('Mosquito Net Double', 'Home & Garden', 25000),
    ('Liquid Soap 5L', 'Home & Garden', 15000), ('Liquid Soap 1L', 'Home & Garden', 4000),
    ('Detergent Powder 2kg', 'Home & Garden', 12000), ('Detergent Powder 500g', 'Home & Garden', 3500),
    ('Wall Clock', 'Home & Garden', 30000), ('Wall Clock Large', 'Home & Garden', 45000),
    ('Bed Sheets', 'Home & Garden', 45000), ('Blanket', 'Home & Garden', 65000),
    ('Towels 2 Pack', 'Home & Garden', 18000), ('Bath Soap 6 Pack', 'Home & Garden', 12000),
    ('Water Jug 20L', 'Home & Garden', 35000), ('Water Bucket', 'Home & Garden', 15000),
    ('Cooking Pot Large', 'Home & Garden', 55000), ('Frying Pan', 'Home & Garden', 25000),
    ('Plates Set 6pc', 'Home & Garden', 18000), ('Cups Set 6pc', 'Home & Garden', 12000),
    ('Floor Mat', 'Home & Garden', 28000), ('Carpet', 'Home & Garden', 75000),
    ('Plant Pot', 'Home & Garden', 8000), ('Garden Hoe', 'Home & Garden', 15000),
    ('Panga Machete', 'Home & Garden', 12000), ('Rake', 'Home & Garden', 10000),
    
    # Stationery
    ('School Backpack', 'Stationery', 45000), ('Laptop Backpack', 'Stationery', 65000),
    ('Hardcover Notebook', 'Stationery', 5000), ('Softcover Notebook', 'Stationery', 3000),
    ('Exercise Book 200pg', 'Stationery', 2000), ('Exercise Book 100pg', 'Stationery', 1200),
    ('Pen Blue', 'Stationery', 1000), ('Pen Black', 'Stationery', 1000),
    ('Pencil HB', 'Stationery', 500), ('Pencil Set', 'Stationery', 5000),
    ('Ruler 30cm', 'Stationery', 1000), ('Eraser', 'Stationery', 500),
    ('Sharpener', 'Stationery', 500), ('Glue Stick', 'Stationery', 2000),
    ('Scissors', 'Stationery', 3000), ('Stapler', 'Stationery', 8000),
    ('Staples', 'Stationery', 1000), ('Paper Clips', 'Stationery', 1000),
    ('Marker Pen', 'Stationery', 2000), ('Highlighter', 'Stationery', 1500),
    ('A4 Paper 500ct', 'Stationery', 15000), ('Manila Paper', 'Stationery', 1000),
    ('Calculator', 'Stationery', 25000), ('Geometry Set', 'Stationery', 8000),
    ('Crayons 12ct', 'Stationery', 4000), ('Water Colors', 'Stationery', 6000),
    ('Pencil Case', 'Stationery', 8000), ('Lunch Box', 'Stationery', 15000),
    
    # Hardware & Tools
    ('Hacksaw', 'Hardware', 12000), ('Hammer', 'Hardware', 8000),
    ('Screwdriver Set', 'Hardware', 15000), ('Pliers', 'Hardware', 7000),
    ('Measuring Tape', 'Hardware', 5000), ('Paint Brush Set', 'Hardware', 8000),
    ('Nails 1kg', 'Hardware', 6000), ('Screws Assorted', 'Hardware', 5000),
    ('Padlock', 'Hardware', 10000), ('Door Handle', 'Hardware', 12000),
    
    # Beauty & Personal Care
    ('Hair Cream', 'Beauty', 8000), ('Shampoo', 'Beauty', 12000),
    ('Conditioner', 'Beauty', 12000), ('Petroleum Jelly', 'Beauty', 5000),
    ('Lotion', 'Beauty', 10000), ('Body Spray', 'Beauty', 15000),
    ('Razor Blades', 'Beauty', 3000), ('Toothpaste', 'Beauty', 4000),
    ('Toothbrush', 'Beauty', 2000), ('Sanitary Pads', 'Beauty', 5000),
    
    # Automotive
    ('Engine Oil 1L', 'Automotive', 18000), ('Engine Oil 4L', 'Automotive', 65000),
    ('Car Battery', 'Automotive', 250000), ('Tire Tube', 'Automotive', 35000),
    ('Air Freshener', 'Automotive', 5000), ('Wiper Blades', 'Automotive', 15000),
    ('Headlight Bulb', 'Automotive', 8000), ('Brake Fluid', 'Automotive', 12000)
]

# --- HELPERS ---
def escape(val: str) -> str:
    return val.replace("'", "''")

def chunked(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

# --- BUILD SQL ---
sql_lines = []
sql_lines.append("-- START OF DATA SEEDING\n")
sql_lines.append("BEGIN;\n")

# =========================
# 1. PRODUCTS
# =========================
sql_lines.append("-- 1. PRODUCTS\n")

product_values = []
for name, cat, price in ugandan_products:
    product_values.append(
        f"('{escape(name)}', '{cat}', {price})"
    )

for chunk in chunked(product_values, 500):
    sql_lines.append(
        "INSERT INTO products (name, category, price) VALUES\n" +
        ",\n".join(chunk) + ";\n"
    )

# =========================
# 2. CUSTOMERS
# =========================
sql_lines.append("\n-- 2. CUSTOMERS\n")

regions = ['Central', 'Western', 'South Western', 'Northern', 'West Nile', 'North Eastern', 'Eastern']
customer_values = []

for _ in range(NUM_CUSTOMERS):
    name = escape(fake.name())
    email = fake.email()
    region = random.choice(regions)
    signup_date = fake.date_between(start_date='-2y', end_date='-1y')

    customer_values.append(
        f"('{name}', '{email}', '{region}', '{signup_date}')"
    )

for chunk in chunked(customer_values, 500):
    sql_lines.append(
        "INSERT INTO customers (name, email, region, signup_date) VALUES\n" +
        ",\n".join(chunk) + ";\n"
    )

# =========================
# 3. ORDERS
# =========================
sql_lines.append("\n-- 3. ORDERS\n")

order_values = []

for _ in range(NUM_ORDERS):
    customer_id = random.randint(1, NUM_CUSTOMERS)
    order_date = fake.date_between(start_date='-1y', end_date='today')

    status = random.choices(
        ['pending', 'completed', 'cancelled'],
        weights=[1, 6, 1]
    )[0]

    order_values.append(
        f"({customer_id}, '{order_date}', '{status}')"
    )

for chunk in chunked(order_values, 500):
    sql_lines.append(
        "INSERT INTO orders (customer_id, order_date, status) VALUES\n" +
        ",\n".join(chunk) + ";\n"
    )

# =========================
# 4. ORDER ITEMS (FIXED MODEL)
# =========================
sql_lines.append("\n-- 4. ORDER ITEMS\n")

order_item_values = []
product_count = len(ugandan_products)

for order_id in range(1, NUM_ORDERS + 1):
    num_items = random.randint(1, 5)  # ensures every order has items

    used_products = set()

    for _ in range(num_items):
        prod_idx = random.randint(0, product_count - 1)

        # avoid duplicate product in same order (optional realism)
        if prod_idx in used_products:
            continue
        used_products.add(prod_idx)

        product_id = prod_idx + 1
        base_price = ugandan_products[prod_idx][2]

        # price variation (±10%)
        unit_price = int(base_price * random.uniform(0.9, 1.1))

        # quantity logic (cheaper → higher qty)
        if base_price < 10000:
            quantity = random.randint(2, 5)
        else:
            quantity = random.randint(1, 2)

        order_item_values.append(
            f"({order_id}, {product_id}, {quantity}, {unit_price})"
        )

for chunk in chunked(order_item_values, 500):
    sql_lines.append(
        "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES\n" +
        ",\n".join(chunk) + ";\n"
    )

# =========================
# FINALIZE
# =========================
sql_lines.append("\nCOMMIT;\n")
sql_lines.append("-- END OF DATA SEEDING\n")

# --- WRITE FILE ---
with open('sample-data.sql', 'w') as f:
    f.write("\n".join(sql_lines))

print(f"✅ SQL file generated successfully!")
print(f"   Customers: {NUM_CUSTOMERS}")
print(f"   Orders: {NUM_ORDERS}")
print(f"   Order Items: {len(order_item_values)}")