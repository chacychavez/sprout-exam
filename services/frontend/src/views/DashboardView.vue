<template>
  <div class="p-5">
  <div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="openAddModal">
      Add new employee
    </button>
    <section v-if="showAddModal">
      <h1>Add new employee</h1>
      <hr/><br/>
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="first_name" class="form-label">First name:</label>
          <input type="text" name="first_name" v-model="form.first_name" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="last_name" class="form-label">Last name:</label>
          <input type="text" name="last_name" v-model="form.last_name" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email:</label>
          <input type="text" name="email" v-model="form.email" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Employee type: </label>
          <select v-model="form.type">
            <option>Regular</option>
            <option>Contractual</option>
          </select>
        </div>
        <div class="mb-3" v-if="form.type === 'Regular'">
          <label for="number_of_leaves" class="form-label">Number of leaves:</label>
          <input type="text" name="number_of_leaves" v-model="form.number_of_leaves" class="form-control" />
        </div>
        
        <div class="mb-3" v-if="form.type === 'Regular'">
          <label for="benefits" class="form-label">Benefits:</label>
          <textarea
            name="benefits"
            v-model="form.benefits"
            class="form-control"
          />
        </div>

        <div class="mb-3" v-if="form.type === 'Contractual'">
          <label for="contract_end_date" class="form-label">Contract end date:</label>
          <input type="date" name="contract_end_date" v-model="form.contract_end_date" class="form-control" />
        </div>
        
        <div class="mb-3" v-if="form.type === 'Contractual'">
          <label for="projects" class="form-label">Projects:</label>
          <textarea
            name="projects"
            v-model="form.projects"
            class="form-control"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Regular Employees</h1>
      <hr/><br/>
      <div v-if="regularEmployees.length" class="row">
        <div v-for="regularEmployee in regularEmployees" :key="regularEmployee.id" class="regularEmployees col-3">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>First name:</strong> {{ regularEmployee.first_name }}</li>
                <li><strong>Last name:</strong> {{ regularEmployee.last_name }}</li>
                <li><strong>Last name:</strong> {{ regularEmployee.email }}</li>
                <li><strong>Number of leaves:</strong> {{ regularEmployee.number_of_leaves }}</li>
                <li><strong>Benefits:</strong> {{ regularEmployee.benefits }}</li>
                <li><router-link :to="{name: 'Employee', params:{type: 'Regular', id: regularEmployee.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>
      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>

    <section>
      <h1>Contractual Employees</h1>
      <hr/><br/>
      <div v-if="contractualEmployees.length" class="row">
        <div v-for="contractualEmployee in contractualEmployees" :key="contractualEmployee.id" class="contractualEmployees col-3">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>First name:</strong> {{ contractualEmployee.first_name }}</li>
                <li><strong>Last name:</strong> {{ contractualEmployee.last_name }}</li>
                <li><strong>Email:</strong> {{ contractualEmployee.email }}</li>
                <li><strong>Contract end date:</strong> {{ contractualEmployee.contract_end_date }}</li>
                <li><strong>Projects:</strong> {{ contractualEmployee.projects }}</li>
                <li><router-link :to="{name: 'Employee', params:{type: 'Contractual', id: contractualEmployee.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>
      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Dashboard',
  data() {
    return {
      showAddModal: false,
      form: {
        first_name: '',
        last_name: '',
        email: '',
        number_of_leaves: '',
        benefits: '',
        type: 'Regular',
        contract_end_date: '',
        projects: ''
      },
    };
  },
  created: function() {
    this.$store.dispatch('getRegularEmployees');
    this.$store.dispatch('getContractualEmployees');
  },
  computed: {
    ...mapGetters({ regularEmployees: 'stateRegularEmployees', contractualEmployees: 'stateContractualEmployees'}),
  },
  methods: {
    ...mapActions(['createRegularEmployee', 'createContractualEmployee']),
    async submit() {
      if (this.form.type ==='Regular') {
        const {first_name, last_name, email, number_of_leaves, benefits} = this.form
        await this.createRegularEmployee({first_name, last_name, email, number_of_leaves, benefits});
      } else {
        const {first_name, last_name, email, contract_end_date, projects} = this.form
        await this.createContractualEmployee({first_name, last_name, email, contract_end_date: new Date(contract_end_date), projects});
      }
    },
    openAddModal() {
      this.showAddModal = true;
    }
  },
});
</script>