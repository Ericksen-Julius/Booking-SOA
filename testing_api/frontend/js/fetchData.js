function getData() {
    const category = ['Hotel', 'Airline', 'Rental', 'Atraksi'];
    let UIType = category[1];  // Adjust this to select the desired category
    let details;
    let info = `
        <img src="./assets/hotel.jpeg" alt="" class="w-100 mb-3">
                <div class="row mb-2">
                    <div class="col-7">
                        Swiss BelHotel Bali
                    </div>
                    <div class="col-1"></div>
                    <div class="col-4 text-primary fw-bolder text-end">
                        Show Map
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-12">
                        Jl. Kubu Anyar No.31, Tuban, Kec. Kuta, Kabupaten Badung
                        4727177
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-12">
                        Bali
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-12">
                        Indonesia
                    </div>
                </div>
                <hr style="border: none; border-top: 2px solid #0d6efd;">
                <div class="row mb-2">
                    <div class="fw-bolder col-12">
                        Got a question?
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-12">
                        +62 123456789
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="text-primary col-12">
                        Email the property
                    </div>
                </div>
                <hr style="border: none; border-top: 2px solid #0d6efd;">
                <div class="row mb-2">
                    <div class="col-12">
                        &#x3F; <span class="fw-bolder">Need Help?</span>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-12 text-primary">
                        Contact customer service
                    </div>
                </div>
            `;

    let book = `
        <div class="row mb-2">
            <div class="col-6 text-center">
                <p class="fw-bolder mb-2">Booking number</p>
                <p>#1261635</p>
            </div>
            <div class="col-6 text-center">
                <p class="fw-bolder mb-2">Payment method</p>
                <p>GoPay</p>
            </div>
        </div>`;

    let recipient = `
        <div class="col-sm-4 col-6 text-center">
            <p class="fw-bolder mb-2">Recipient name</p>
            <p>Yan Witanto</p>
        </div>
        <div class="col-sm-4 col-6 text-center">
            <p class="fw-bolder mb-2">Phone number</p>
            <p>08182738263</p>
        </div>
        <div class="col-sm-4 col-12 text-center">
            <p class="fw-bolder mb-2">Email address</p>
            <p>yan@gmail.com</p>
        </div>`;

    if (UIType === 'Hotel') {
        details = `
            <div class="col-sm-3 col-12 m-0 mb-2">
                <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
            </div>
            <div class="col-sm-9 col-12">
                <div class="row mb-2">
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Room Type</p>
                        <p>VIP</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Night(s)</p>
                        <p>2</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Quantity</p>
                        <p>4</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Price</p>
                        <p>Rp. 15,000,000</p>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Check-in</p>
                        <p>Sat, June 1 2024</p>
                    </div>
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Check-out</p>
                        <p>Sat, June 3 2024</p>
                    </div>
                </div>
            </div>`;
    } else if (UIType === 'Airline') {
        details = `
            <div class="col-sm-3 col-12 m-0 mb-2">
                <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
            </div>
            <div class="col-sm-9 col-12">
                <div class="row mb-2">
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Flight class</p>
                        <p>Economy</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Flight code</p>
                        <p>#456</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Quantity</p>
                        <p>4</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Price</p>
                        <p>Rp. 15,000,000</p>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Departure time</p>
                        <p>Sat, June 1 2024 10:00 PM</p>
                    </div>
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Arrival time</p>
                        <p>Sat, June 3 2024 12:00 PM</p>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-6">
                        <p class="fw-bolder mb-2">From</p>
                        <p>Surabaya</p>
                    </div>
                    <div class="col-6">
                        <p class="fw-bolder mb-2">To</p>
                        <p>Jakarta</p>
                    </div>
                </div>
            </div>`;
    } else if (UIType === 'Rental') {
        details = `
            <div class="col-sm-3 col-12 m-0 mb-2">
                <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
            </div>
            <div class="col-sm-9 col-12">
                <div class="row mb-2">
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Car</p>
                        <p>Kijang Innova</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Day(s)</p>
                        <p>3</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Quantity</p>
                        <p>4</p>
                    </div>
                    <div class="col-3">
                        <p class="fw-bolder mb-2">Price</p>
                        <p>Rp. 15,000,000</p>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Pick Up Date</p>
                        <p>Sat, June 1 2024</p>
                    </div>
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Return Date</p>
                        <p>Sat, June 4 2024</p>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Pick Up Location</p>
                        <p>Jl. Kubu Anyar No.31, Tuban, Kec. Kuta, Kabupaten Badung 4727177</p>
                    </div>
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Return Location</p>
                        <p>Jl. Kubu Anyar No.31, Tuban, Kec. Kuta, Kabupaten Badung 4727177</p>
                    </div>
                </div>
            </div>`;
    } else {
        details = `
            <div class="col-sm-3 col-12 m-0 mb-2">
                <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
            </div>
            <div class="col-sm-9 col-12">
                <div class="row mb-2">
                    <div class="col-4">
                        <p class="fw-bolder mb-2">Type</p>
                        <p>Terusan</p>
                    </div>
                    <div class="col-4">
                        <p class="fw-bolder mb-2">Quantity</p>
                        <p>4</p>
                    </div>
                    <div class="col-4">
                        <p class="fw-bolder mb-2">Price</p>
                        <p>Rp. 15,000,000</p>
                    </div>
                </div>
                <div class="row mb-2">
                    <div class="col-6">
                        <p class="fw-bolder mb-2">E-ticket number</p>
                        <p>#345</p>
                    </div>
                    <div class="col-6">
                        <p class="fw-bolder mb-2">Visit</p>
                        <p>Sat, June 4 2024</p>
                    </div>
                </div>
            </div>`;
    }
    document.getElementById('detailContainer').innerHTML = details;
    document.getElementById('infoContainer').innerHTML = info;
    document.getElementById('bookContainer').innerHTML = book;
    document.getElementById('recipientContainer').innerHTML = recipient;
}

document.addEventListener('DOMContentLoaded', (event) => {
    getData();
});

