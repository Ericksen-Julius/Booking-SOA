localStorage.setItem('userID', 1);

document.addEventListener('DOMContentLoaded', (event) => {
    const params = new URLSearchParams(window.location.search);
    const service_id = params.get('service_id');
    const get_visit_date = params.get('visit_date');
    const packet_attraction_id = params.get('paket_attraction_id');
    const total_price = document.getElementById('total_price');
    const ticket_price = document.getElementById('ticket_price')
    const provider_name = document.getElementsByClassName('provider_name')
    const visit_date = document.getElementById('visit_date')
    const address = document.getElementById('address')
    const paket_type = document.getElementsByClassName('paket_type')
    const schedule = document.getElementById('schedule')
    const carousel_wrapper = document.getElementById('carousel_wrapper')
    const rating = document.getElementById('rating')
    const class_visit_date = document.getElementsByClassName('class_visit_date')
    const count = document.getElementById('count')
    const ticket_price_1 = document.getElementById('ticket_price_1')
    const submitButton = document.getElementById('book')
    const service_url = ''
    let ticketPriceValue = 0
    let totalPriceValue = 0
    let providerName = 'Dufan'


    console.log(get_visit_date)
    console.log(packet_attraction_id)
    console.log(service_id)

    const dateVisit = new Date(get_visit_date);

    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    const dayOfVist = days[dateVisit.getDay()];
    const dayOfVisit = dateVisit.getDate();
    const monthOfVisit = months[dateVisit.getMonth()];
    const yearOfVisit = dateVisit.getFullYear();;

    visit_date.innerHTML = `${dayOfVist}, ${dayOfVisit} ${monthOfVisit} ${yearOfVisit}`;
    class_visit_date.innerHTML = `${dayOfVist}, ${dayOfVisit} ${monthOfVisit} ${yearOfVisit}`;



    async function getTicketData() {
        console.log("uhuy")
        // try {
        //     const response = await fetch(`http://52.200.174.164:8003/service/${service_id}`, {
        //         method: 'GET',
        //     });

        //     if (!response.ok) {
        //         throw new Error(`HTTP error! Status: ${response.status}`);
        //     }
        //     const result = await response.json()
        //     service_url = result.data.service_url

        // } catch (error) {
        //     console.error('Error:', error);
        // }

        try {
            const urlReview = `http://3.226.141.243:8004/reviewRating/${providerName}`
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
            const url = `${service_url}/api/atrkasi/`
            const response = await fetch(`http://3.217.250.166:8003/api/atraksi`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            // console.log('Success:', result);
            console.log(result)
            for (let i = 0; i < provider_name.length; i++) {
                provider_name[i].innerHTML = result.title
            }
            address.innerHTML = result.alamat
            const formattedOpeningHours = formatOpeningHours(result.jam_buka);
            console.log(formattedOpeningHours);
            schedule.innerHTML = formattedOpeningHours
            let imageCarousel
            result.photo.forEach(element => {
                if (imageCarousel == null) {
                    imageCarousel = `<div class="carousel-item active">
                                        <img src="${element.image}" class="d-block w-100" alt="${element.placeholder}">
                                    </div>`
                } else {
                    imageCarousel += `<div class="carousel-item">
                                        <img src="${element.image}" class="d-block w-100" alt="${element.placeholder}">
                                    </div>`
                }
            });
            console.log(imageCarousel)
            carousel_wrapper.innerHTML = imageCarousel
        } catch (error) {
            console.error('Error:', error);
        }

        try {
            const url = `${service_url}/api/atraksi/paket/${packet_attraction_id}`
            const response = await fetch(`http://3.217.250.166:8003/api/atraksi/paket/1`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            // console.log('Success:', result);
            console.log(result)
            ticket_price.innerHTML = `Rp. ${formatRupiah(result.harga)}`
            for (let i = 0; i < paket_type.length; i++) {
                paket_type[i].innerHTML = result.title
            }
            ticket_price_1.innerHTML = `Rp. ${formatRupiah(result.harga)}`
            count.innerHTML = `(${counterValue}x)`
            ticketPriceValue = result.harga
            updateTotalPrice()
        } catch (error) {
            console.error('Error:', error);
        }
    }

    function formatOpeningHours(jamBuka) {
        if (!jamBuka || jamBuka.length === 0) {
            return "Closed";
        }

        // const days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"];
        const openDays = jamBuka.filter(day => day.is_open === 1).map(day => day.hari);

        if (openDays.length === 7) {
            // If all days are open, use the general format
            return `Open | Senin-Minggu, ${jamBuka[0].waktu}`;
        } else {
            // Otherwise, create a string of open days
            const openDaysString = openDays.join(",");
            const openingTime = jamBuka[0].waktu; // Assuming waktu is the same for all days
            return `Open | ${openDaysString}, ${openingTime}`;
        }
    }

    // Example data similar to your provided example
    // const jamBuka = [
    //     { "hari": "Senin", "waktu": "09:00 - 17:00", "is_open": 1 },
    //     { "hari": "Selasa", "waktu": "09:00 - 17:00", "is_open": 1 },
    //     { "hari": "Rabu", "waktu": "09:00 - 17:00", "is_open": 1 },
    //     { "hari": "Kamis", "waktu": "09:00 - 17:00", "is_open": 1 },
    //     { "hari": "Jumat", "waktu": "09:00 - 17:00", "is_open": 1 },
    //     { "hari": "Sabtu", "waktu": "09:00 - 17:00", "is_open": 1 },
    //     { "hari": "Minggu", "waktu": "09:00 - 17:00", "is_open": 1 }
    // ];

    // Call the function with example data



    const counterElement = document.getElementById('counter');
    const decreaseButton = document.getElementById('decrease');
    const increaseButton = document.getElementById('increase');

    let counterValue = 1
    decreaseButton.addEventListener('click', () => {
        if (counterValue > 1) {
            counterValue--;
            counterElement.innerHTML = counterValue;
            count.innerHTML = `(${counterValue}x)`
            updateTotalPrice();
        }
    });

    increaseButton.addEventListener('click', () => {
        counterValue++;
        counterElement.innerHTML = counterValue;
        count.innerHTML = `(${counterValue}x)`
        updateTotalPrice();
    });

    function updateTotalPrice() {
        totalPriceValue = ticketPriceValue * counterValue;
        total_price.innerHTML = `Rp. ${formatRupiah(totalPriceValue)}`;
    }

    async function postBookingAttraction() {
        const data = {
            user_id: user_id,
            type: "Attraction",
            total_price: totalPriceValue,
            provider_name: providerName,
            paket_attraction_id: packet_attraction_id,
            visit_date: get_visit_date,
            number_of_tickets: counterValue,
            service_id: service_id
        };
        const user_id = localStorage.getItem('userID');

        try {
            const urlPost = `http://3.226.141.243:8004/booking`
            const response1 = await fetch(`http://localhost:8000/booking`, {
                method: 'POST',
                body: JSON.stringify(data)
            });
            if (!response1.ok) {
                throw new Error(`HTTP error! Status: ${response1.status}`);
            }
            const result1 = await response1.json();
            if (result1.status == 200) {
                const url2 = `${service_url}/api/eticket`
                const data1 = {
                    _token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidGlwZW4ifQ.bFPsfkx60z4QfIGTJNgrB4nRBtF727hN6lUGIp1u9Nw",
                    paket_id: packet_attraction_id,
                    jml_ticket: counterValue,
                    booking_code: result1.booking_code,
                    tgl_booking: get_visit_date
                };
                const response2 = await fetch(`http://3.217.250.166:8003/api/eticket`, {
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
                        // if (result.isConfirmed) {
                        //     window.location.href = `http://3.226.141.243:8004/paymentTempatAtraksi.php?booking_code=${result1.booking_code}&booking_id=${result1.booking_id}`;
                        // }
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
            type: "Attraction",
            total_price: totalPriceValue,
            provider_name: providerName,
            paket_attraction_id: packet_attraction_id,
            visit_date: get_visit_date,
            number_of_tickets: counterValue,
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
    getTicketData()
    submitButton.addEventListener('click', function () {
        if (isDateInThePast(get_visit_date)) {
            Swal.fire({
                title: "Failed",
                text: "Invalid date!",
                icon: "error"
            })
            return
        }
        postBookingAttraction()
    })
    function isDateInThePast(dateString) {
        const inputDate = new Date(dateString);

        const currentDate = new Date();

        return inputDate < currentDate;
    }

});


function formatRupiah(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
