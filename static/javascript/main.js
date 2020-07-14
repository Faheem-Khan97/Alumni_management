const navSlide = () =>
{

    //console.log(10);
    const burger = document.querySelector('.burger');

    const nav = document.querySelector('.nav-links');

    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click',() =>
    {
        //console.log(10);
        nav.classList.toggle('nav-active');

        //Animate

        navLinks.forEach((link , index) =>
        {
            //console.log(link, index);
            if(link.style.animation)
            {
                link.style.animation ='';
            }
            else
            {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index/5 + 0.3}s`;
            }
    
        });
        //Burger animation

        burger.classList.toggle('toggle');


    });


}

navSlide();