// https://stripe.com/docs/js/appendix/style
// https://stripe.com/docs/elements/appearance-api

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
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

// Handle validation errors 

card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </span>
            <span>${event.error.message}</span>
        `
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// 

// If you disable collecting fields in the Payment Element, you
// must pass equivalent data when calling `stripe.confirmPayment`.
let form = document.getElementById('payment-form')

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };

    let url = '/checkout/cache_checkout_data/'
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                },
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            },
        })
            .then(function (result) {
                if (result.error) {
                    let errorDiv = document.getElementById('card-errors');
                    let html = `
                <span class="icon" role="alert">
                    <i class="fa-solid fa-triangle-exclamation"></i>
                </span>
                <span>${result.error.message}</span>
                `;
                    $(errorDiv).html(html);
                    card.update({ 'disabled': false });
                    $('#submit-button').attr('disabled', false);
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
    }).fail(function(){
        location.reload();
    })
});