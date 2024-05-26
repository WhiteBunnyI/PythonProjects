import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wgt


# Скрывает отображение осей и тиков
def hideAxe(axe):
    axe.spines['top'].set_visible(False)
    axe.spines['bottom'].set_visible(False)
    axe.spines['right'].set_visible(False)
    axe.spines['left'].set_visible(False)
    axe.get_xaxis().set_ticks([])
    axe.get_yaxis().set_ticks([])


# Начальные значения
freq1, freq2, amp1, amp2 = 1, 1, 1, 1
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = np.sin(freq1 * x) * amp1
y2 = np.sin(freq2 * x) * amp2
y3 = y1 + y2

# Создаем оси
fig, axs = plt.subplot_mosaic([['param1', 'wave1', 'wave1'],
                               ['param2', 'wave2', 'wave2'],
                               ['', 'wave3', 'wave3']],
                              figsize=(12, 8))
line1, = axs['wave1'].plot(x, y1, color='blue')
line2, = axs['wave2'].plot(x, y2, color='green')
line3, = axs['wave3'].plot(x, y3, color='pink')

# Удаляем ось
fig.delaxes(axs[''])
hideAxe(axs['param1'])
hideAxe(axs['param2'])

# Разделяем оси на 2 оси
ax_freq1 = axs['param1'].inset_axes([0, 0.7, 0.9, 0.2])
ax_amp1 = axs['param1'].inset_axes([0, 0.3, 0.9, 0.2])

ax_freq2 = axs['param2'].inset_axes([0, 0.7, 0.9, 0.2])
ax_amp2 = axs['param2'].inset_axes([0, 0.3, 0.9, 0.2])

# Настравиваем оси
axs['wave1'].set_ylim([-5, 5])
axs['wave2'].set_ylim([-5, 5])
axs['wave3'].set_ylim([-5, 5])

# Создаем ползунки
slider_freq1 = wgt.Slider(ax_freq1, 'freq', 0, 10, valinit=freq1, orientation='horizontal')
slider_amp1 = wgt.Slider(ax_amp1, 'amp', 0, 10, valinit=amp1, orientation='horizontal')

slider_freq2 = wgt.Slider(ax_freq2, 'freq', 0, 10, valinit=freq1, orientation='horizontal')
slider_amp2 = wgt.Slider(ax_amp2, 'amp', 0, 10, valinit=amp1, orientation='horizontal')


# Функция для обновления данных
def update(event):
    freq1 = slider_freq1.val
    freq2 = slider_freq2.val

    amp1 = slider_amp1.val
    amp2 = slider_amp2.val

    y1 = np.sin(freq1 * x) * amp1
    y2 = np.sin(freq2 * x) * amp2
    y3 = y1 + y2

    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line3.set_ydata(y3)

    fig.canvas.draw_idle()


slider_freq1.on_changed(update)
slider_amp1.on_changed(update)
slider_freq2.on_changed(update)
slider_amp2.on_changed(update)

plt.show()
