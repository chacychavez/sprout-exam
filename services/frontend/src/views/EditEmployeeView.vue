<template>
  <div class="p-5">
    <section>
      <h1>Edit note</h1>
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
        <div class="mb-3" v-if="type === 'Regular'">
          <label for="number_of_leaves" class="form-label">Number of leaves:</label>
          <input type="text" name="number_of_leaves" v-model="form.number_of_leaves" class="form-control" />
        </div>
        <div class="mb-3" v-if="type === 'Regular'">
          <label for="benefits" class="form-label">benefits:</label>
          <textarea
            name="benefits"
            v-model="form.benefits"
            class="form-control"
          ></textarea>
        </div>
        <div class="mb-3" v-if="type === 'Contractual'">
          <label for="contract_end_date" class="form-label">Contract end date:</label>
          <input type="date" name="contract_end_date" v-model="form.contract_end_date" class="form-control" />
        </div>
        <div class="mb-3" v-if="type === 'Contractual'">
          <label for="projects" class="form-label">Projects:</label>
          <textarea
            name="projects"
            v-model="form.projects"
            class="form-control"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'EditEmployee',
  props: ['type', 'id'],
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        email: '',
        number_of_leaves: '',
        benefits: '',
        contract_end_date: '',
        projects: ''
      },
    };
  },
  created: function() {
    this.GetEmployee();
  },
  computed: {
    ...mapGetters({ regularEmployee: 'stateRegularEmployee', contractualEmployee: 'stateContractualEmployee',}),
  },
  methods: {
    ...mapActions(['updateRegularEmployee', 'viewRegularEmployee', 'updateContractualEmployee', 'viewContractualEmployee']),
    async submit() {
      try {
        const {
          first_name,
          last_name,
          email,
          number_of_leaves,
          benefits,
          contract_end_date,
          projects
        } = this.form
        let employee = {
          id: this.id,
          form: this.type === 'Regular' ? {first_name, last_name, email, number_of_leaves, benefits} : {first_name, last_name, email, contract_end_date: new Date(contract_end_date).getTime() / 1000, projects},
        };
        if (this.type === 'Regular') {
          await this.updateRegularEmployee(employee);
          this.$router.push({name: 'Employee', params:{type: this.type, id: this.regularEmployee.id}});
        }
        else {
          console.log(typeof employee.form.contract_end_date)
          await this.updateContractualEmployee(employee);
          this.$router.push({name: 'Employee', params:{type: this.type, id: this.contractualEmployee.id}});
        }
      } catch (error) {
        console.log(error);
      }
    },
    async GetEmployee() {
      try {
        if (this.type === 'Regular') {
          await this.viewRegularEmployee(this.id);
          this.form = this.regularEmployee;
        }
        else {
          await this.viewContractualEmployee(this.id);
          this.form = this.contractualEmployee;
          const currDate = new Date(this.form.contract_end_date)
          var day = ("0" + currDate.getDate()).slice(-2);
          var month = ("0" + (currDate.getMonth() + 1)).slice(-2);

          var out = currDate.getFullYear()+"-"+(month)+"-"+(day) ;
          this.form.contract_end_date = out;
        }
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    }
  },
});
</script>