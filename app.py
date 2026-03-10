from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('splash.html')

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
    return render_template('home.html')

@app.route('/qr')
def qr():
    return render_template('qr.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/card_payment')
def card_payment():
    return render_template('card_payment.html')

@app.route('/reward')
def reward():
    return render_template('reward.html')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/favorites')
def favorites():
    """Favorites page with user's saved items"""
    return render_template('favorites.html',)
@app.route('/topup')
def topup():
    """Favorites page with user's saved items"""
    return render_template('topup.html',)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)