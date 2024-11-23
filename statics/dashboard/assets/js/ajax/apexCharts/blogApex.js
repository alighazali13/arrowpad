Apex.grid = {
    borderColor: '#191e3a'
}
Apex.track = {
    background: '#0e1726',
}
Apex.tooltip = {
    theme: 'dark'
}
window.addEventListener("load", (event) => {
    const blogUrl = document.getElementById('blog_url').value;

    const data = {
        'blogUrl' : blogUrl,
    }
    console.log(data)
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            // if not safe, set csrftoken
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
            };
        }
    });
    // Sending data from validation
    $.ajax({
        url : '/analytics/blogs/manage/getBlogView/' ,
        type : "POST" ,
        data : {
            'getdata' : JSON.stringify(data)
        } ,
        dataType : 'json' ,
        success : function (res , status) {
            console.log('res');
            console.log(getShamsiMonthBefore(12));
            views = res.views
            console.log(views)
            
            var sline = {
                chart: {
                  height: 350,
                  type: 'line',
                  zoom: {
                    enabled: false
                  },
                  toolbar: {
                    show: false,
                  }
                },
                dataLabels: {
                  enabled: false
                },
                stroke: {
                  curve: 'straight'
                },
                series: [{
                  name: "بازدید",
                  data: views
                }],
                title: {
                  text: 'بازدید یک سال گذشته',
                  align: 'right',
                  offsetX: -120,
                },
                grid: {
                  row: {
                    colors: ['#3b3f5c', 'transparent'], // takes an array which will be repeated on columns
                    opacity: 0.5
                  },
                },
                xaxis: {
                  categories: getShamsiMonthBefore(12),
                },
                yaxis: {
                  labels: {
                    offsetX: -20,
                  }
                }
              
              }
              
              var chart = new ApexCharts(
                document.querySelector("#s-line"),
                sline
              );
              
              chart.render().then(() => {
                attachClickEvents();
              });
            
        } ,
        error : function () {
            console.log('er')
            
        } ,
    });
});


function getShamsiMonthBefore(monthsToSubtract) {
  const monthsInPersian = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'];

  // تاریخ امروز میلادی
  const today = new Date();

  // دریافت جزئیات تاریخ میلادی
  const gDate = today.getDate();
  const gMonth = today.getMonth() + 1; // ماه میلادی بین 0 و 11 است
  const gYear = today.getFullYear();

  // محاسبه تاریخ شمسی
  let jYear, jMonth;
  if (gMonth <= 3) {
      jYear = gYear - 622;
      jMonth = gMonth + 9; // ماه‌های ابتدایی
  } else {
      jYear = gYear - 621;
      jMonth = gMonth - 3; // ماه‌های باقی‌مانده
  }

  // ایجاد آرایه‌ای برای ذخیره ماه‌های گذشته
  let monthsBefore = [];

  for (let i = 0; i < monthsToSubtract; i++) {
      let newMonth = jMonth - (i + 1);

      // اگر ماه منفی شد، به سال قبل می‌رویم
      while (newMonth <= 0) {
          newMonth += 12; // ماه‌ها را به سال قبل منتقل می‌کنیم
          jYear -= 1; // سال را یک واحد کاهش می‌دهیم
      }

      // به جای استفاده از newMonth، از newMonth - 1 استفاده می‌کنیم تا به درستی به ماه‌های گذشته دسترسی پیدا کنیم
      monthsBefore.push(monthsInPersian[(newMonth) % 12]);
  }

  return monthsBefore;
}


// // function attachClickEvents() {
// //     document.querySelectorAll("text.apexcharts-xaxis-label").forEach(item => {
// //       const firstChild = item.firstElementChild; // گرفتن اولین فرزند
// //       month = firstChild.textContent
// //       // firstChild.setAttribute('onclick', `monthredirect('${month}')`);
// //       firstChild.setAttribute('onclick', `alert('${month}')`);
// //       console.log(firstChild);
      
// //   });
// // }

// // function monthredirect(month) {
// //   alert(month)
// // }


// // document.addEventListener("DOMContentLoaded", function() {
// //   attachClickEvents();
// // });

