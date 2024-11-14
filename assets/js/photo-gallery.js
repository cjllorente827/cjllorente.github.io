function drawPhotos(){

    var $photo_gallery = $(".photo-gallery");
    var $modal = $(".modal");
    var $img_container = $(".image_container");

    var img_scale_factor = 0.3;

    $img_container.hide();

    $modal.click(()=>{
        $img_container.hide();
        $img_container.html("");
        $modal.hide();
    });

    $modal.hide();
    
    

    for (let i = 0; i < 392; i++){


        var thumb_url = `assets/images/cats/water_tribe/thumbs/water_tribe_${i.toString().padStart(4, "0")}.jpg`;
        let img_url = `assets/images/cats/water_tribe/water_tribe_${i.toString().padStart(4, "0")}.jpg`;
        var $cell = $(`<div class="photo-gallery-cell" style="background-image:url(${thumb_url})"> </div>`);
        $photo_gallery.append($cell);

        

        $cell.hover(() => {
            //console.log(`Hover over ${i}`);
        });

        $cell.click(() => {

            console.log(img_url);
            var $img = $('<img src="'+ img_url +'">');
            $img.on("load", function(e) {

                var $this = $(this);
                var [w,h] = [window.outerWidth, document.documentElement.clientHeight];
                console.log(w, h);
                var center = {
                    x: w/2,
                    y: h/2
                };

                var [img_w, img_h] = [this.width * img_scale_factor, this.height * img_scale_factor];

                var [img_x, img_y] = [
                    center.x - img_w/2,
                    center.y - img_h/2,
                ];

                $this.width(this.width * img_scale_factor);
                $this.height(this.height * img_scale_factor);
                $this.appendTo($img_container);
                $img_container.css({"top":`${img_y}px`,"left":`${img_x}px`});
                $img_container.show();
            });
            
            $modal.show();
        });
    }
    
}