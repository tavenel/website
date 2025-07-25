export class HiddenSelect {

	private selectId: string;
	private showButtonId: string;

	constructor(selectId: string, showButtonId: string) {
		this.selectId = selectId;
		this.showButtonId = showButtonId;
	}

	setDefault(defaultValue: string) {

		if (!defaultValue) {
			return;
		}

		const selectElt = document.getElementById(this.selectId) as HTMLSelectElement;
		selectElt.value = defaultValue;
	}

	addChangeListener(callback: any) {

		const selectElt = document.getElementById(this.selectId) as HTMLSelectElement;
		if (!selectElt) {
			console.error('Unable to find select element with ID: ', this.selectId);
			return false;
		}

		selectElt.addEventListener("change", (event: Event) => {
			const selectValue = (event.target as HTMLSelectElement).value;
			callback(selectValue);
		});

	}

	addShowButtonListener() {
		const selectId = this.selectId;

		const showButton = document.getElementById(this.showButtonId);
		if (!showButton) {
			console.error('Unable to find select button with ID: ', this.showButtonId);
			return false;
		}
		showButton.addEventListener("click", function () {
			const selectElt = document.getElementById(selectId);
			if (!selectElt) {
				console.error('Unable to find select element with ID: ', selectId);
				return false;
			}
			const selectClass = selectElt.classList;
			if (selectClass.contains('hidden')) {
				selectClass.remove('hidden');
			} else {
				selectClass.add('hidden');
			}

		});
	}

}
