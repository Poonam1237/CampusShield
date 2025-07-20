
window.addEventListener('scroll',()=>
{
    let el=document.querySelectorAll('.fade')
    let el2=document.querySelectorAll('.fade1')
    let el3=document.querySelectorAll('.move')
    let el4=document.querySelectorAll('.back')

    let wh=window.innerHeight;

    el.forEach((e)=>
    {
        let p=e.getBoundingClientRect().top;

        if(p<wh-100)
        {
            e.classList.add('active')
        }

        else
        {
            e.classList.remove('active')
        }
    })

    el2.forEach((e)=>
    {
        let p=e.getBoundingClientRect().top;

        if(p<wh-100)
        {
            e.classList.add('active')
        }

        else
        {
            e.classList.remove('active')
        }
    })


     el3.forEach((e)=>
    {
        let p=e.getBoundingClientRect().top;

        if(p<wh-100)
        {
            e.classList.add('m1')
        }

        else
        {
            e.classList.remove('m1')
        }
    })

    el4.forEach((e)=>
    {
        let p=e.getBoundingClientRect().top;

        if(p<wh-100)
        {
            e.classList.add('b1')
        }

        else
        {
            e.classList.remove('b1')
        }
    })
})