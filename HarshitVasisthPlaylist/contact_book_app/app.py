from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store contacts
contact_book = {}

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Add Contact route
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        if len(phone_no) == 10:
            contact_book[name] = phone_no
            return redirect(url_for('view_contacts'))
        else:
            return "Enter a valid phone number with 10 digits."
    return render_template('add_contact.html')

# View Contacts route
@app.route('/view')
def view_contacts():
    return render_template('view_contacts.html', contacts=contact_book)

# Update Contact route
@app.route('/update', methods=['GET', 'POST'])
def update_contact():
    if request.method == 'POST':
        name = request.form['name']
        new_phone_no = request.form['new_phone_no']
        if name in contact_book:
            if len(new_phone_no) == 10:
                contact_book[name] = new_phone_no
                return redirect(url_for('view_contacts'))
            else:
                return "Enter a valid phone number with 10 digits."
        else:
            return "Contact not found."
    return render_template('update_contact.html')

# Delete Contact route
@app.route('/delete/<name>')
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        return redirect(url_for('view_contacts'))
    return "Contact not found."

# Search Contact route
@app.route('/search', methods=['GET', 'POST'])
def search_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone_no = contact_book.get(name)
        if phone_no:
            return f"Contact found: {name} - {phone_no}"
        else:
            return "Contact not found."
    return render_template('search_contact.html')

if __name__ == '__main__':
    app.run(debug=True)
