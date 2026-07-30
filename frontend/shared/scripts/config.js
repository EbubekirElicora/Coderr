const GUEST_LOGINS = {
    customer: {
        username: 'Demo-Kunde',
        password: 'DemoPassword123!'
    },
    business: {
        username: 'Demo-Anbieter',
        password: 'DemoPassword123!'
    }
};

const IS_LOCAL = ['localhost', '127.0.0.1'].includes(
    window.location.hostname
);

const API_BASE_URL = IS_LOCAL
    ? 'http://127.0.0.1:8000/api/'
    : '/api/';

const STATIC_BASE_URL = IS_LOCAL
    ? 'http://127.0.0.1:8000/'
    : '/';

const LOGIN_URL = 'login/';

const REGISTER_URL = 'registration/';

const PROFILE_URL = 'profile/';

const BUSINESS_PROFILES_URL = 'profiles/business/';

const CUSTOMER_PROFILES_URL = 'profiles/customer/';

const REVIEW_URL = 'reviews/';

const ORDER_URL = 'orders/';

const OFFER_URL = 'offers/';

const OFFER_DETAIL_URL = 'offerdetails/';

const BASE_INFO_URL = 'base-info/';

const OFFER_INPROGRESS_COUNT_URL = 'order-count/';
const OFFER_COMPLETED_COUNT_URL = 'completed-order-count/';

const PAGE_SIZE = 6