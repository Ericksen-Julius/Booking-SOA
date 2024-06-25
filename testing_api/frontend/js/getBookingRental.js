
document.addEventListener('DOMContentLoaded', (event) => {
    const params = new URLSearchParams(window.location.search);
    const service_id = params.get('service_id');
    const pickup = params.get('pickup');
    const get_return_date = params.get('return');
    const car_id = params.get('car_id');
    const car_image = document.getElementById('car_image');
    const seats = document.getElementById('seats')
    const luggages = document.getElementById('luggages')
    const transmission = document.getElementById('transmission')
    const year = document.getElementById('year')
    const rental_price = document.getElementById('rental_price')
    const car_name = document.getElementsByClassName('car_name')
    const day_rental = document.getElementById('day_rental')
    const total_price = document.getElementById('total_price')
    const provider_name = document.getElementById('provider_name')
    const rating = document.getElementById('rating')
    const image_wrapper = document.getElementById('image_wrapper')
    const pick_up_date = document.getElementById('pick_up_date')
    const return_date = document.getElementById('return_date')
    const service_url = ''
    let providerName = 'Yanto Car'

    console.log(service_id)
    console.log(pickup)
    console.log(get_return_date)
    console.log(car_id)


    const dateObjectCheckIn = new Date(pickup);
    const dateObjectCheckOut = new Date(get_return_date);

    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    const dayOfWeekCheckIn = days[dateObjectCheckIn.getDay()];
    const dayOfMonthCheckIn = dateObjectCheckIn.getDate();
    const monthCheckIn = months[dateObjectCheckIn.getMonth()];
    const yearCheckIn = dateObjectCheckIn.getFullYear();
    const dayOfWeekCheckOut = days[dateObjectCheckOut.getDay()];
    const dayOfMonthCheckOut = dateObjectCheckOut.getDate();
    const monthCheckOut = months[dateObjectCheckOut.getMonth()];
    const yearCheckOut = dateObjectCheckOut.getFullYear();

    pick_up_date.innerHTML = `${dayOfWeekCheckIn}, ${dayOfMonthCheckIn} ${monthCheckIn} ${yearCheckIn}`;
    return_date.innerHTML = `${dayOfWeekCheckOut}, ${dayOfMonthCheckOut} ${monthCheckOut} ${yearCheckOut}`;

    const checkIn = new Date(pickup);
    const checkOut = new Date(get_return_date);

    const differenceMs = Math.abs(checkOut - checkIn);

    const dayRental = Math.ceil(differenceMs / (1000 * 60 * 60 * 24));

    day_rental.innerHTML = dayRental == 1 ? `(${dayRental} day)` : `(${dayRental} days)`


    async function getCarData() {
        try {
            const response = await fetch(`http://52.200.174.164:8003/service/${service_id}`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json()
            provider_name.innerHTML = result.data.provider_name
            service_url = result.data.service_url
        } catch (error) {
            console.error('Error:', error);
        }

        try {
            const response = await fetch(`http://localhost:8000/reviewRating/${providerName}`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json()
            console.log(result)
            rating.innerHTML = `${result.average_rating}/5 <span
                            class="text-dark">(${result.total_reviewers})</span>`
        } catch (error) {
            console.error('Error:', error);
        }

        try {
            const url = `${service_url}/car/${car_id}}`
            const response = await fetch(url, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            // console.log('Success:', result);
            console.log(result)
            car_image.src = result.image
            seats.innerHTML = result.data.car_seats
            luggages.innerHTML = result.data.car_seats
            transmission.innerHTML = result.data.car_seats
            year.innerHTML = result.data.car_seats
            rental_price.innerHTML = `Rp. ${formatRupiah(result.data.car_price)}`
            for (let i = 0; i < car_name.length; i++) {
                car_name[i].innerHTML = result.data.car_name
            }
            image_wrapper.src = result.image
            total_price.innerHTML = `Rp. ${formatRupiah(result.data.car_price)}`

            updateTotalPrice()
        } catch (error) {
            console.error('Error:', error);
        }
    }
    getCarData()

});


function formatRupiah(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
