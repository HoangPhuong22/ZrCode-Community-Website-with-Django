// get search form add page links
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('btn-page')

// ensure search form exits 
if(searchForm)
{
    for(let i = 0 ; i < pageLinks.length ; i++)
    {
        pageLinks[i].addEventListener('click', function(e) {
            e.preventDefault();
            let page = this.dataset.page
            // add hidden input page
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            // submit form
            searchForm.submit()
        })
    }
}