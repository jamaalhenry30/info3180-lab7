<template>
    <form  @submit.prevent="uploadPhoto" id="uploadForm">
        <div class="form-group">
            <label for="" class="col-sm-2 coml-form-label">Description</label>
            <div class="">
                <textarea name = "description" type="" class="form-control" id="" placeholder="Enter Description"></textarea>
            </div>
        </div>
       <div class="form-group" id="filediv">
            <div class="custom-file">
                <input name = "photo" type="file" class="form-control" id="customFile">
            </div>
        </div>
        <div class="form-group" id="buttdiv">
            <div class="col-sm-10 ">
                <button class="btn btn-primary">Upload</button>
            </div>

        </div>
    </form>
</template>

<script>
    export default {
        data(){
            return{
                csrf_token:''

            }
        },
        created(){
            this.getCsrfToken();
        },
        methods:{
            uploadPhoto(){
                let uploadForm = document.getElementById("uploadForm"); 
                let form_data = new FormData(uploadForm);

                fetch("/api/upload", { 
                    method: "POST",
                    body: form_data,
                    headers:{
                        'X-CSRFToken':this.csrf_token
                    }
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) { 
                     // display a success message
                     console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
            getCsrfToken(){
                let self = this;
                fetch('/api/csrf-token')
                    
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
            }
        }
    }

</script>

<style>
#filediv{
    margin-top: 20px;
}
#buttdiv{
    margin-top: 10px;
}
</style>