<script>

    import { deleteCompany } from "../../stores/admin/companies/deletecompany";
    import { updateCompany } from "../../stores/admin/companies/updatecompany";

    export let company;
    export let token;
    export let isEditing = false;

    let updatedCompany = {
        "id": company.id,
        "name": company.name,
        "description": company.description,
        "address": company.address,
        "city": company.city,
        "zipcode": company.zipcode,
        "url_website": company.url_website,
    }

    async function toggleEditing() {
        isEditing = !isEditing;
        if(!isEditing){
            console.log(updatedCompany)
            console.log(await updateCompany(token, updatedCompany));
        }
    }

  function Delete(token, id){
    console.log(deleteCompany(token, id));
  }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{company.id}</p>
            {#if isEditing}
                <input type="text" bind:value={updatedCompany.name} />
                <input type="text" class="description" bind:value={updatedCompany.description} />
                <input type="text" bind:value={updatedCompany.address} />
                <input type="text" bind:value={updatedCompany.city} />
                <input type="text" bind:value={updatedCompany.zipcode} />
                <input type="text" bind:value={updatedCompany.url_website} />
            {:else}
                <p>{updatedCompany.name}</p>
                <p class="description">{updatedCompany.description}</p>
                <p>{updatedCompany.address}</p>
                <p>{updatedCompany.city}</p>
                <p>{updatedCompany.zipcode}</p>
                <p>{updatedCompany.url_website}</p>
            {/if}
            <button class="edit" on:click={toggleEditing}><img src="/src/assets/stylo.png" alt="Edit"></button>
            <button class="delete" on:click={Delete(token, company.id)}><img src="/src/assets/corbeille.png" alt="Delete"></button>
         </div>
    </div>

</main>

<style>

@media screen and (max-width: 1024px){
    .row{
        overflow-x: scroll;
    }
}

.container{
    padding: 10px;
    margin: 15px;
    border-radius: 10px;
    background-color: #f1f1f1;
    border: 2px solid #f7f7f7;
}

.container:hover{
    background-color: #eaeaea;
}

.description{
    overflow-y: scroll;
    grid-column-start: 3;
    grid-column-end: 5;
}

.row{
    display: grid;
    grid-template-columns: repeat(9, 1fr) repeat(2, 0.3fr);
    gap: 10px;
    height: 60px;
}



img{
    width: 20px;
    filter: brightness(0) invert(1);
}

button{
    cursor: pointer;
    padding: 10px;
    margin: 5px;
    border-radius: 10px;
    background-color: white;
    /* box-shadow: 0px 3px 5px 0px rgba(0,0,0,0.15); */
    border: none;
    width: 55px;
}


.edit{
    background-color: rgb(118, 255, 182);
    border: 2px solid #f7f7f7;
    grid-column-start: 10;
}

.delete{
    background-color: rgb(255, 118, 118);
    border: 2px solid #f7f7f7;
    grid-column-start: 11;
}

.delete:hover{
    background-color: rgb(255, 148, 148);
}

.edit:hover{
    background-color: rgb(148, 255, 182);
}



</style>