/** layuiAdmin.std-v1.0.0 LPPL License By http://www.layui.com/admin/ */
;layui.define(function (e) {
    var a = layui.admin;
    layui.use(["admin", "carousel"], function () {
        var e = layui.$, a = (layui.admin, layui.carousel), l = layui.element, t = layui.device();
        e(".layadmin-carousel").each(function () {
            var l = e(this);
            a.render({
                elem: this,
                width: "100%",
                arrow: "none",
                interval: l.data("interval"),
                autoplay: l.data("autoplay") === !0,
                trigger: t.ios || t.android ? "click" : "hover",
                anim: l.data("anim")
            })
        }), l.render("progress")
    }),


        layui.use(["carousel", "echarts"], function () {
            d = undefined;
            layui.$.ajax({
                url: 'http://127.0.0.1:8000/api/project',
                method: 'get',
                success: function (data) {
                    var e = layui.$, a = (layui.carousel, layui.echarts), l = [], t = [{
                        title: {text: "用例数据统计", subtext: ""},
                        tooltip: {trigger: "axis"},
                        calculable: !0,
                        legend: {data: ["用例数", "执行次数"]},
                        xAxis: [{
                            type: "category",
                            data: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
                        }],
                        yAxis: [{type: "value"}],
                        series: [{
                            name: "用例数",
                            type: "bar",
                            data: [2, 4.9, 7, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20, 6.4, 3.3],
                        }, {
                            name: "执行次数",
                            type: "bar",
                            data: [2.6, 5.9, 9, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6, 2.3],
                        }]
                    }], i = e("#LAY-index-normcol").children("div"), n = function (e) {
                        l[e] = a.init(i[e], layui.echartsTheme), l[e].setOption(t[e]), window.onresize = l[e].resize
                    };
                    i[0] && n(0)
                }
            });


        })
});