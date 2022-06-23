// https://stripe.com/docs/js/appendix/style
// https://stripe.com/docs/elements/appearance-api

let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let stripe_client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let card = elements.create('card', {
    style: {
        base: {
          iconColor: '#0C0809',
          color: '#0C0809',
          fontWeight: '500',
          fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
          fontSize: '16px',
          fontSmoothing: 'antialiased',
          ':-webkit-autofill': {
            color: '#fce883',
          },
          '::placeholder': {
            color: '#6c757d',
          },
        },
        invalid: {
          iconColor: '#C42021',
          color: '#C42021',
        },
      },
    });   
card.mount('#card-element');