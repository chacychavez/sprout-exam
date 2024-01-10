import { createStore } from "vuex";

import employees from './modules/employees';
import users from './modules/users';

export default createStore({
    modules: {
        employees,
        users,
    }
});