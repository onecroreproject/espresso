from flask import Flask, render_template, redirect, url_for, request, jsonify
import os
import json

app = Flask(__name__)

RATES_FILE = 'rates.json'

def get_rates():
    if not os.path.exists(RATES_FILE):
        default_rates = {"bd": 1.0, "usd": 0.377, "eur": 0.35}
        with open(RATES_FILE, 'w') as f:
            json.dump(default_rates, f)
        return default_rates
    with open(RATES_FILE, 'r') as f:
        return json.load(f)

def save_rates(rates):
    with open(RATES_FILE, 'w') as f:
        json.dump(rates, f)

@app.route('/')
def loading():
    return render_template('loading.html')
@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.route('/allproject')
def allproject():
    rates = get_rates()
    return render_template('allproject.html', rates=rates)

@app.route('/productdetails')
def productdetails():
    rates = get_rates()
    return render_template('productdetails.html', rates=rates)

@app.route('/register-splash')
def register_splash():
    return render_template('register-splash.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/otp')
def otp():
    return render_template('otp.html')

@app.route('/home')
def home():
    rates = get_rates()
    return render_template('home.html', rates=rates)

@app.route('/qr')
def qr():
    return render_template('qr.html')

@app.route('/menu')
def menu():
    rates = get_rates()
    return render_template('menu.html', rates=rates)

@app.route('/order')
def order():
    rates = get_rates()
    return render_template('order.html', rates=rates)

@app.route('/payment')
def payment():
    rates = get_rates()
    return render_template('payment.html', rates=rates)

@app.route('/card_payment')
def card_payment():
    rates = get_rates()
    return render_template('card_payment.html', rates=rates)

@app.route('/reward')
def reward():
    rates = get_rates()
    return render_template('reward.html', rates=rates)

@app.route('/wallet')
def wallet():
    rates = get_rates()
    return render_template('wallet.html', rates=rates)

@app.route('/profile')
def profile():
    rates = get_rates()
    return render_template('profile.html', rates=rates)

@app.route('/settings')
def settings():
    rates = get_rates()
    return render_template('settings.html', rates=rates)

@app.route('/update_rates', methods=['POST'])
def update_rates():
    data = request.json
    rates = {
        "bd": float(data.get('bd', 1.0)),
        "usd": float(data.get('usd', 0.377)),
        "eur": float(data.get('eur', 0.35))
    }
    save_rates(rates)
    return jsonify({"status": "success", "rates": rates})

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/change_password')
def change_password():
    return render_template('change_password.html')

@app.route('/delete_account')
def delete_account():
    return render_template('delete_account.html')


@app.route('/favorites')
def favorites():
    """Favorites page with user's saved items"""
    rates = get_rates()
    return render_template('favorites.html', rates=rates)
@app.route('/topup')
def topup():
    """Top up wallet page"""
    rates = get_rates()
    return render_template('topup.html', rates=rates)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)