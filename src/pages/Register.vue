<template>
  <!-- <div v-if="jobs.length">
  <div v-for="job in jobs" :key="job.id" class="job">
    <h1>{{job.title}}</h1>
  </div>
  </div>
  <div v-else><p>Loading Details</p></div> -->
    <div class="row">
      <div class="column left">
        <p>Plant as much as you can</p>
      </div>
      <div class="column right">
        <div class="q-pa-md" style="max-width: 400px">
        <div v-if="errors.length > 0">
      <ul>
        <li v-for="item in errors" :key="item">{{item}}</li>
      </ul>
    </div>
    <div v-if="isSuccess">Registered Successfully</div>
    <div v-if="error"><h5>Email is already exists</h5></div>
    <q-form
      @submit.prevent="addNote"
      class="q-gutter-md"
    >
      <q-input
        filled
        v-model="fname"
        label="Your first name *"
        hint="First Name"
        lazy-rules
        :rules="[ val => val && val.length > 2 || 'Please type your first name']"
      />

      <q-input
        filled
        v-model="lname"
        label="Your last name *"
        hint="Surname"
        lazy-rules
        :rules="[ val => val && val.length > 2 || 'Please type your last name']"
      />

      <q-input
        filled
        type="email"
        v-model="email"
        label="Your email *"
        hint="Your email"
        lazy-rules
        :rules="[ val => val && val.length > 10 || 'Please type your email']"
      />
      
      <q-input
        filled
        type="password"
        v-model="password"
        label="Your password *"
        hint="Your password"
        lazy-rules
        :rules="[ val => val && val.length > 0 && val.length < 10 || 'Please type your password']"
      />

      <q-input
        filled
        type="password"
        v-model="repassword"
        label="Re-enter your password *"
        hint="Confirm your password"
        lazy-rules
        :rules="[ val => val && val.length > 0 && val.length < 10|| 'Please type your password']"
      />

      <div>
        <center><q-btn label="Submit" type="submit" color="primary"/></center>
        <!-- <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" /> -->
       </div>
    </q-form>
    </div>
      </div>
    </div>
    
</template>

<script>
import axios from 'axios'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'
import { ref } from 'vue'

export default {

   data() {
    return {
      fname:'',
      lname:'',
      email:'',
      password:'',
      repassword:'',
      isSuccess:false,
      post_data:null,
      jobs:[],
      errors:[],
      error: '',

    }
  },
  mounted() {
    fetch('http://127.0.0.1:8000/api/tasks/')
    //.then(res=>res.json())
    .then(data=>this.jobs=data)
    .catch(err=>console.log(err.message))
  },
  methods: {
    load_data() {
      api.get('http://127.0.0.1:8000/api/tasks/').then((resp) => {
          this.post_data = resp.data;
        })
    },
    addNote() {
      this.errors=[]
      if(this.password!==this.repassword) {
        this.errors.push("the passwords are not equal")
        alert("Passwords are not equal")
      }
      
      api.post('http://127.0.0.1:8000/api/tasks/',
      {fname:this.fname,lname:this.lname,email:this.email,password:this.password,repassword:this.repassword},)
      .then((res) => {
        //thsi.token = res.data.token;
        //console.log(this.token)
        //localStorage.setItem('user-token',res.data.token)
        console.log(res);
        this.isSuccess=true
        this.info = res.statusText;
        this.$router.push('/');
      }) 
      .catch((err)=>console.log(this.error=err.message));
      //localStorage.removeItem('user-token')
      //alert("Emailis already registered");
      //this.error.value = err.data
      },      
    
  },
  created() {
    this.load_data();
  } 
}
  /*setup () {
    const $q = useQuasar()

    const fname = ref(null)
    const lname = ref(null)
    const fnameRef = ref(true)
    const lnameRef = ref(true)

    const email = ref(null)
    const emailRef = ref(true)

    const password = ref(null)
    const passRef = ref(true)

    const repassword = ref(null)
    const repassRef = ref(true)

    const accept = ref(false)
  
    return {
      text: ref(''),
      fname,
      lname,
      nameRules: [
        val => (val && val.length > 0) || 'Please type your name'
      ],

      email,
      emailRef,
      emailRules: [
        val => (val !== null && val !== '') || 'Please type your email',
        //val => (val > 0 && val < 100) || 'Please type a real age'
      ],

      password,
      passRef,
      passwordRules: [
        val => (val !== null && val !== '') || 'Please type your password',
      ],

      repassword,
      repassRef,
      repasswordRules: [
        val => (val !== null && val !== '') || 'Please type your password',
      ],
      accept,
      isSuccess:false,
      addNote () {
        

        axios.post('http://127.0.0.1:8000/api/tasks/',
        {fname:this.fname,lname:this.lname,email:this.email,password:this.password,repassword:this.repassword},)
        .then((resp)=> {
          this.isSuccess = true;
          console.log(resp);
        });

        if (fnameRef.value.hasError || lnameRef.value.hasError || emailRef.value.hasError || passRef.value.hasError || repassRef.value.hasError) {
          // form has error
        }
        else if (accept.value !== true) {
          $q.notify({
            color: 'negative',
            message: 'You need to accept the license and terms first'
          })
        }
        
      },

      onReset () {
        fname.value = null
        lname.value = null
        email.value = null
        password.value = null
        repassword.value = null

        fnameRef.value.resetValidation()
        lnameRef.value.resetValidation()
        emailRef.value.resetValidation()
        passRef.value.resetValidation()
        repassRef.value.resetValidation()
      }
    }
  },*/

</script>

<style scoped>
.my-custom-image{
  filter: blur(1px) sepia();
}
.column{
  float:left;
  width:50%;
  padding:10px;
  height:90vh;
}
.row:after{
  
  display:table;
  clear:both;
}
.left{
  background-image:url('../assets/registerimg.jpg');
  background-repeat: no-repeat;
  background-size:cover;
  background-position: center;
}
p{
  text-align:center;
  padding-top:20%;
  font-size:100px;
  color:lightgreen;
}
</style>
