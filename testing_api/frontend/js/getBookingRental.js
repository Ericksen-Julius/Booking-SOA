localStorage.setItem('userID', 1);
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
    const rental_price = document.getElementsByClassName('rental_price')
    const car_name = document.getElementsByClassName('car_name')
    const day_rental = document.getElementById('day_rental')
    const total_price = document.getElementById('total_price')
    const provider_name = document.getElementById('provider_name')
    const rating = document.getElementById('rating')
    const image_wrapper = document.getElementById('image_wrapper')
    const pick_up_date = document.getElementById('pick_up_date')
    const return_date = document.getElementById('return_date')
    const insuranceCheckbox2 = document.getElementById('insuranceCheckbox2');
    const pick_up_location = document.getElementById('pickup');
    const return_location = document.getElementById('return');
    const is_with_driver = 0
    let asuransi_id = 0
    let service_url = ''
    const submitButton = document.getElementById('book')
    const carInsurance = document.getElementById('insuranceCheckbox1')

    let providerName = 'Yanto Car'
    let totalPriceValue = 100000
    let insurance_price = 0
    let pricelist
    total_price.innerHTML = `Rp. ${formatRupiah(totalPriceValue)}`

    console.log(service_id)
    console.log(pickup)
    console.log(get_return_date)
    console.log(car_id)

    if (!car_id || !service_id || !pickup || !get_return_date) {
        document.body.innerHTML = '<h1>Access Denied</h1>';
        return;
    }


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

    insuranceCheckbox2.addEventListener('click', () => {
        is_with_driver = insuranceCheckbox2.checked ? 1 : 0;
        console.log('Checkbox state:', is_with_driver);
        // You can now use the `checkboxState` variable as needed
    });

    carInsurance.addEventListener('click', () => {
        asuransi_id = carInsurance.checked ? 1 : 0;
        console.log(insurance_price)
        if (asuransi_id == 1) {
            totalPriceValue += insurance_price
        } else {
            totalPriceValue -= insurance_price
        }
        total_price.innerHTML = `Rp. ${formatRupiah(totalPriceValue)}`
        console.log(totalPriceValue)
        // You can now use the `checkboxState` variable as needed
    });

    async function getInsurancePrice() {
        try {
            const response = await fetch(`http://ec2-52-7-154-154.compute-1.amazonaws.com:8005/insurance/all`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json()
            console.log(result)
            pricelist = result.filter(insurance => insurance.id_car == car_id);
            console.log(pricelist)
            const keys = Object.keys(pricelist[0]);

            for (let i = 4; i < keys.length; i++) {
                console.log(keys[i].toString())
                const [min, max] = keys[i].toString().split('-').map(Number);
                console.log(min)
                if (dayRental >= min && dayRental <= max) {
                    insurance_price = pricelist[0][keys[i]]
                    break
                }
            }
            // console.log(insurance_price)
        } catch (error) {
            console.error('Error:', error);
        }
    }

    getInsurancePrice()


    async function getCarData() {
        console.log("check")
        try {
            const response = await fetch(`http://107.20.145.163:8003/carrental/service/${service_id}/pickup/-/returncar/-/car_id/-`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json()
            provider_name.innerHTML = result.data.service_name
            providerName = result.data.service_name
            service_url = result.data.url
        } catch (error) {
            console.error('Error:', error);
        }

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
            seats.innerHTML = `<i class="fa-solid fa-chair"></i> ${result.data.car_seats} seats`
            luggages.innerHTML = `<i class="fa-solid fa-suitcase"></i> ${result.data.car_seats} luggages`
            transmission.innerHTML = `<i class="fa-solid fa-cogs"></i> ${result.data.car_transmission}`
            year.innerHTML = `<i class="fa-solid fa-certificate"></i> ${result.data.car_year}`
            totalPriceValue = result.data.car_price
            // rental_price.innerHTML = `Rp. ${formatRupiah(result.data.car_price)}`
            for (let i = 0; i < rental_price.length; i++) {
                rental_price[i].innerHTML = `Rp. ${formatRupiah(result.data.car_price)}`
            }
            for (let i = 0; i < car_name.length; i++) {
                car_name[i].innerHTML = result.data.car_name
            }
            image_wrapper.src = result.image
            total_price.innerHTML = `Rp. ${formatRupiah(result.data.car_price)}`

        } catch (error) {
            console.error('Error:', error);
        }
    }
    // getCarData()

    function isDateInThePast(dateString) {
        const inputDate = new Date(dateString);

        const currentDate = new Date();

        return inputDate < currentDate;
    }

    async function postBookingRental() {
        if (pick_up_location.value == '' || return_location.value == '') {
            Swal.fire({
                title: "Failed",
                text: "Tempat pengambilan dan pengembalian harus diisi!",
                icon: "error"
            }).then((result) => {
                if (result.isConfirmed) {
                    return
                }
            })
            return
        }
        if (isDateInThePast(pickup) | isDateInThePast(get_return_date)) {
            Swal.fire({
                title: "Failed",
                text: "Invalid date!",
                icon: "error"
            }).then((result) => {
                if (result.isConfirmed) {
                    return
                }
            })
            return
        }
        const user_id = localStorage.getItem('userID');
        const data = {
            user_id: parseInt(user_id),
            type: "Rental",
            total_price: totalPriceValue,
            provider_name: providerName,
            car_id: parseInt(car_id),
            pick_up_date: pickup,
            return_date: get_return_date,
            pick_up_location: pick_up_location.value,
            return_location: return_location.value,
            is_with_driver: is_with_driver,
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
                const url2 = `${service_url}/booking_add`
                const data1 = {
                    tanggal_mulai: pickup,
                    tanggal_selesai: get_return_date,
                    with_driver: is_with_driver,
                    total_harga: totalPriceValue,
                    car_id: parseInt(car_id)
                };
                const response2 = await fetch(`http://3.228.174.120:8001/booking_add`, {
                    method: 'POST',
                    body: JSON.stringify(data1)
                });
                const result = await response2.json()
                console.log(result)
                if (!response2.ok) {
                    throw new Error(`HTTP error! Status: ${response2.status}`);
                } else {
                    Swal.fire({
                        title: "Success",
                        text: "Booking success!",
                        icon: "success"
                    }).then((result) => {
                        if (result.isConfirmed) {
                            // window.location.href = `/paymentRental.php?booking_code=${result1.booking_code}&booking_id=${result1.booking_id}`;
                        }
                    });
                }

            }

        } catch (error) {
            console.error('Error:', error);
        }

    }
    getCarData()

    async function coba() {

        const data = {
            user_id: 1,
            type: "Rental",
            total_price: totalPriceValue,
            provider_name: providerName,
            car_id: car_id,
            asuransi_id: asuransi_id,
            pick_up_date: pickup,
            return_date: get_return_date,
            pick_up_location: pick_up_location.value,
            return_location: return_location.value,
            is_with_driver: is_with_driver,
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
        postBookingRental()
    })

});


function formatRupiah(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
