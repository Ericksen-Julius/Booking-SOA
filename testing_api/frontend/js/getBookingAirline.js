
document.addEventListener('DOMContentLoaded', (event) => {
    const params = new URLSearchParams(window.location.search);
    const service_id = params.get('service_id');
    const flight_date = params.get('flight_date');
    const flight_code = params.get('flight_code');
    const provider_name = document.getElementsByClassName('provider_name');
    const rating = document.getElementById('rating')
    const ticket_price = document.getElementById('ticket_price');
    const insurance = document.getElementById('insurance');
    const insurance_price = document.getElementById('insurance_price');
    const total_price = document.getElementById('total_price');
    const customer_name = document.getElementById('customer_name');
    const origin = document.getElementsByClassName('origin')
    const destination = document.getElementsByClassName('destination')
    const flight_date_1 = document.getElementById('flight_date')
    const flight_type = document.getElementById('flight_type')
    const origin_airport = document.getElementById('origin_airport')
    const destination_airport = document.getElementById('destination_airport')
    const departure_time = document.getElementById('departure_time')
    const arrival_time = document.getElementById('arrival_time')
    const capacity = document.getElementById('capacity')
    const submitButton = document.getElementById('book')
    const weight = document.getElementById('weight')
    const travelInsuranceCheck = document.getElementById('travelInsuranceCheck')
    const service_url = ''
    let insurancePrice = 0
    let asuransi_id = 0
    let ticketPrice = 0
    let totalPriceValue = 0
    let providerName = 'Garuda Indonesia'

    console.log(service_id)
    console.log(flight_date)
    console.log(flight_code)


    const dateObjectDeparture = new Date(flight_date);

    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    const dayOfDeparture = days[dateObjectDeparture.getDay()];
    const dayOfMonthDeparture = dateObjectDeparture.getDate();
    const monthDeparture = months[dateObjectDeparture.getMonth()];
    const yearDeparture = dateObjectDeparture.getFullYear();

    flight_date_1.innerHTML = `${dayOfDeparture}, ${dayOfMonthDeparture} ${monthDeparture} ${yearDeparture}`;

    const flights = [
        {
            "flight_code": "GA 208",
            "airport_origin_name": "Soekarno-Hatta Intl",
            "airport_origin_location_code": "CGK",
            "airport_origin_city_name": "Jakarta",
            "airport_destination_name": "New Yogyakarta Int.",
            "airport_destination_location_code": "YIA",
            "airport_destination_city_name": "Yogyakarta",
            "start_time": "17:30:00",
            "end_time": "18:50:00",
            "class_name": "Business Class",
            "capacity": 50,
            "price": 3000000,
            "date": "2024-06-12",
            "weight": 30,
            "delay": 0
        },
        {
            "flight_code": "ID 123",
            "airport_origin_name": "Bandung Airport",
            "airport_origin_location_code": "BDO",
            "airport_origin_city_name": "Bandung",
            "airport_destination_name": "Surabaya Airport",
            "airport_destination_location_code": "SUB",
            "airport_destination_city_name": "Surabaya",
            "start_time": "13:30:00",
            "end_time": "15:50:00",
            "class_name": "Economy",
            "capacity": 100,
            "price": 1000000,
            "date": "2024-08-12",
            "weight": 50,
            "delay": 0
        },
        {
            "flight_code": "QR 1456",
            "airport_origin_name": "New Yogyakarta Int.",
            "airport_origin_location_code": "YIA",
            "airport_origin_city_name": "Yogyakarta",
            "airport_destination_name": "Bandung Airport",
            "airport_destination_location_code": "BDO",
            "airport_destination_city_name": "Bandung",
            "start_time": "14:30:00",
            "end_time": "15:50:00",
            "class_name": "Economy",
            "capacity": 50,
            "price": 5000000,
            "date": "2024-06-12",
            "weight": 30,
            "delay": 0
        }
    ];

    const result = flights.filter(flight => flight.flight_code === "QR 1456");

    travelInsuranceCheck.addEventListener('click', () => {
        asuransi_id = travelInsuranceCheck.checked ? 1 : 0;

        if (asuransi_id == 1) {
            totalPriceValue += insurance_price
        } else {
            totalPriceValue -= insurance_price
        }
        total_price.innerHTML = `Rp. ${formatRupiah(totalPriceValue)}`
        // You can now use the `checkboxState` variable as needed
    });

    async function getFlightData() {
        // try {
        //     const response = await fetch(`http://52.200.174.164:8003/service/${service_id}`, {
        //         method: 'GET',
        //     });

        //     if (!response.ok) {
        //         throw new Error(`HTTP error! Status: ${response.status}`);
        //     }
        //     const result = await response.json()
        //     provider_name.forEach(element => {
        //         element.innerHTML = result.data.provider_name
        //     });
        //     service_url = result.data.service_url

        // } catch (error) {
        //     console.error('Error:', error);
        // }

        try {
            const urlReview = `http://3.226.141.243:8004/reviewRating/${providerName}`
            const response = await fetch(urlReview, {
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
        console.log(result[0])
        ticket_price.innerHTML = `Rp. ${formatRupiah(result[0].price)}`
        insurance_price.innerHTML = `Rp. ${formatRupiah(insurancePrice)}`
        total_price.innerHTML = `Rp. ${formatRupiah(result[0].price)}`
        for (let i = 0; i < origin.length; i++) {
            origin[i].innerHTML = result[0].airport_origin_city_name
        }
        for (let i = 0; i < destination.length; i++) {
            destination[i].innerHTML = result[0].airport_destination_city_name
        }
        flight_type.innerHTML = result[0].class_name
        origin_airport.innerHTML = result[0].airport_origin_location_code
        destination_airport.innerHTML = result[0].airport_destination_location_code
        departure_time.innerHTML = result[0].start_time
        arrival_time.innerHTML = result[0].end_time
        capacity.innerHTML = result[0].capacity
        weight.innerHTML = result[0].weight
        totalPriceValue += result[0].price

        // try {
        //     const url = `${service_url}/hotel/room_type/${room_id}`
        //     const response = await fetch(`http://52.200.174.164:8003/hotel/room_type/1`, {
        //         method: 'GET',
        //     });

        //     if (!response.ok) {
        //         throw new Error(`HTTP error! Status: ${response.status}`);
        //     }

        //     const result = await response.json();
        //     // console.log('Success:', result);
        //     console.log(result)
        //     room_price.innerHTML = `Rp. ${formatRupiah(result.price)}`
        //     room_type.innerHTML = result.type
        //     roomPriceValue = result.price
        //     provider_name.innerHTML = providerName
        //     image_wrapper.src = result.image
        //     room_price_1.innerHTML = `Rp. ${formatRupiah(result.price)}`
        //     count.innerHTML = `(${counterValue}x)`

        //     updateTotalPrice()
        // } catch (error) {
        //     console.error('Error:', error);
        // }

    }
    getFlightData()

    async function postBookingAirline() {
        const data = {
            user_id: 1,
            type: "Airline",
            total_price: totalPriceValue,
            provider_name: providerName,
            asuransi_id: asuransi_id == -1 ? null : asuransi_id,
            flight_id: flight_code,
            flight_date: flight_date,
            service_id: service_id
        };
        try {
            const urlPost = `http://3.226.141.243:8004/booking`
            const response1 = await fetch(urlPost, {
                method: 'POST',
                body: JSON.stringify(data)
            });
            if (!response1.ok) {
                throw new Error(`HTTP error! Status: ${response1.status}`);
            }
            const result1 = await response1.json();
            if (result1.status == 200) {
                const url2 = `${service_url}/post_ticket`
                const data1 = {
                    customer_name: customer_name.value,
                    flight_code: flight_code,
                    flight_date: flight_date
                };
                const response2 = await fetch(url2, {
                    method: 'POST',
                    body: JSON.stringify(data1)
                });

                if (!response2.ok) {
                    throw new Error(`HTTP error! Status: ${response2.status}`);
                } else {
                    Swal.fire({
                        title: "Success",
                        text: "Booking success!",
                        icon: "success"
                    }).then((result) => {
                        if (result.isConfirmed) {
                            window.location.href = `http://3.226.141.243:8004/payment.php?booking_code=${result1.booking_code}`;
                        }
                    });
                }

            }

        } catch (error) {
            console.error('Error:', error);
        }
    }

    async function coba() {
        const data = {
            user_id: 1,
            type: "Airline",
            total_price: totalPriceValue,
            provider_name: providerName,
            asuransi_id: asuransi_id,
            flight_id: flight_code,
            flight_date: flight_date,
            service_id: service_id
        };
        try {
            const urlPost = `http://localhost:8000/booking`
            const response1 = await fetch(urlPost, {
                method: 'POST',
                body: JSON.stringify(data)
            });
            if (!response1.ok) {
                throw new Error(`HTTP error! Status: ${response1.status}`);
            }
            const result1 = await response1.json();
            console.log(result1)
        } catch (error) {

        }
    }

    submitButton.addEventListener('click', function () {
        console.log('check')
        coba()
    })

});


function formatRupiah(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
