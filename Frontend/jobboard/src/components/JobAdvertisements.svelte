<script>
    import { getJobsAdvertisements } from "../stores/jobadvertisements";

    export let job;
    export let token;
    export let rhView = false;

    let promise;

    async function getJobAdvertisement(){
        promise = await getJobsAdvertisements(job.id);
    }

    function apply(){
        console.log('apply', job.id);
        window.location.href = '/apply?id=' + job.id;
    }

</script>

<main>


    <div class="container">
        <div class="title">
        <h3>{job.contract_type} - {job.title} </h3>
        </div>
        {#if !rhView}
            <span>Company : {job.company_name}</span><br>
        {:else}
            <span>Date of publication : {job.date_of_jobadvertisements}</span><br>
            <span>Published by : {job.firstname} {job.lastname}</span><br>

        {/if}
        <span>Location : {job.location}</span><br><br>
        <div>
            <details on:toggle|once={getJobAdvertisement}>
                <summary>Learn more</summary>

                <div class="details">

                    {#if promise}    
                        <p>{promise.description}</p>
                        {#if !rhView}
                            <button class="applying" on:click={apply}>Apply</button>
                        {/if}
                    {:else}
                        <p>Loading</p>
                    {/if}


                </div>
            </details>
        </div>
    </div>

</main>

<style>

    .container{
        padding: 10px;
        margin: 15px;
        border-radius: 10px;
        background-color: #f1f1f1;
        transition: transform 0.3s, border 0.3s;
        border: 2px solid #f7f7f7;
    }

    .applying{
        margin-top: 10px;
        background-color: rgb(140, 0, 255);
        color: white;
        border: none;
        border-radius: 5px;
    }

    .applying:hover{
        cursor: pointer;
        background-color: rgb(179, 0, 255);
    }

    .title{
        background-color: white;
        padding: 10px;
        border-radius: 10px;
    }

    summary:hover{
        cursor: pointer;
    }

    .container:hover{
        transform: scale(1.03);
        border: 2px solid rgb(140, 0, 255);
    }

    button{
        padding: 10px 20px;
        margin: 5px;

    }

</style>