import axios from 'axios';

const state = {
  regularEmployees: [],
  regularEmployee: null,
  contractualEmployees: [],
  contractualEmployee: null
};

const getters = {
  stateRegularEmployees: state => state.regularEmployees,
  stateRegularEmployee: state => state.regularEmployee,
  stateContractualEmployees: state => state.contractualEmployees,
  stateContractualEmployee: state => state.contractualEmployee,
};

const actions = {
  async createRegularEmployee({dispatch}, regularEmployee) {
    await axios.post('employees/regular', regularEmployee);
    await dispatch('getRegularEmployees');
  },
  async getRegularEmployees({commit}) {
    let {data} = await axios.get('employees/regular');
    commit('setRegularEmployees', data);
  },
  async viewRegularEmployee({commit}, id) {
    let {data} = await axios.get(`employees/regular/${id}`);
    commit('setRegularEmployee', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateRegularEmployee({}, regularEmployee) {
    await axios.patch(`employees/regular/${regularEmployee.id}`, regularEmployee.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteRegularEmployee({}, id) {
    await axios.delete(`employees/regular/${id}`);
  },
  async createContractualEmployee({dispatch}, contractualEmployee) {
    await axios.post('employees/contractual', contractualEmployee);
    await dispatch('getContractualEmployees');
  },
  async getContractualEmployees({commit}) {
    let {data} = await axios.get('employees/contractual');
    commit('setContractualEmployees', data);
  },
  async viewContractualEmployee({commit}, id) {
    let {data} = await axios.get(`employees/contractual/${id}`);
    commit('setContractualEmployee', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateContractualEmployee({}, contractualEmployee) {
    await axios.patch(`employees/contractual/${contractualEmployee.id}`, contractualEmployee.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteContractualEmployee({}, id) {
    await axios.delete(`employees/contractual/${id}`);
  }
};

const mutations = {
  setRegularEmployees(state, regularEmployees){
    state.regularEmployees = regularEmployees;
  },
  setContractualEmployees(state, contractualEmployees){
    state.contractualEmployees = contractualEmployees;
  },
  setRegularEmployee(state, regularEmployee){
    state.regularEmployee = regularEmployee;
  },
  setContractualEmployee(state, contractualEmployee){
    state.contractualEmployee = contractualEmployee;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};