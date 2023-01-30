class PixelMapper:
	def __init__(self, ownerComp):
		self.ownerComp 			= ownerComp
		self.pixel_strip_table 	= self.ownerComp.op('pixel_strip_table')

		print('Pixel Mapper class initialized from {}.'.format(self.ownerComp.name))
		print('- '*30)
		pass 

#region Pixel Strip
	def Add_pixel_strip(self):
		if self.ownerComp.par.Serpentine == True:
			self.pixel_strip_table.appendRow([	self.pixel_strip_table.numRows,
												self.ownerComp.par.Length, 
												self.ownerComp.par.Numpixels,
												self.get_strip_direction(),
												self.ownerComp.par.Vertical,
												self.get_strip_position()
											])
		elif self.ownerComp.par.Serpentine == False:
			self.pixel_strip_table.appendRow([	self.pixel_strip_table.numRows,
												self.ownerComp.par.Length, 
												self.ownerComp.par.Numpixels,
												0,
												self.ownerComp.par.Vertical,
												self.get_strip_position()
											])
		pass 

	def get_strip_direction(self):
		serpentine = 0 
		if self.pixel_strip_table.numRows == 1:
			serpentine = 0
			pass 
		if self.pixel_strip_table.numRows > 1:

			if self.pixel_strip_table[int(self.pixel_strip_table.numRows-1), 'flipped'].val == '0':
				serpentine = 1
				pass 

			if self.pixel_strip_table[int(self.pixel_strip_table.numRows-1), 'flipped'].val == '1':
				serpentine = 0 
				pass 
			pass 

		return serpentine

	def get_strip_position(self):
		strip_pos = 0
		if self.pixel_strip_table.numRows == 1:
			strip_pos = 0
			pass 
		if self.pixel_strip_table.numRows == 2:
			strip_pos = float(self.pixel_strip_table[1, 'pos'].val) + self.ownerComp.par.Gaptostrip
			pass 
		if self.pixel_strip_table.numRows > 2:
			strip_pos = float(self.pixel_strip_table[self.pixel_strip_table.numRows-1, 'pos'].val) + self.ownerComp.par.Gaptostrip
		return strip_pos

	def Create_pixel_strip_op(self):
		num_ops = len(self.ownerComp.findChildren(type=lineSOP))# + self.ownerComp.findChildren(type=addSOP))
		if num_ops >= self.pixel_strip_table.numRows-1:
			print('No pixel row specified for new strip.')
			print('- '*30)
			pass 
		else:
			new_op = self.ownerComp.create(lineSOP)
			new_op.nodeX = 0
			new_op.nodeY = 0 - (150 * num_ops-1)
			new_op.outputConnectors[0].connect(parent().op('merge1'))
			if num_ops < 2:
				if self.pixel_strip_table[num_ops+1, 'vertical'] == 'False':
					if self.pixel_strip_table[num_ops+1, 'flipped'] == '0':
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * - 1"
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass 
					elif self.pixel_strip_table[num_ops+1, 'flipped'] == '1':
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * -1"
						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass 
				elif self.pixel_strip_table[num_ops+1, 'vertical'] == 'True':
					if self.pixel_strip_table[num_ops+1, 'flipped'] == '0':
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * - 1"
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass 
					elif self.pixel_strip_table[num_ops+1, 'flipped'] == '1':
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * -1"
						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass 
				pass 
			if num_ops > 1:
				if self.pixel_strip_table[num_ops+1, 'vertical'] == 'False':
					if self.pixel_strip_table[num_ops+1, 'flipped'] == '0':
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * - 1"
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass 
					elif self.pixel_strip_table[num_ops+1, 'flipped'] == '1':
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * -1"
						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass 
				elif self.pixel_strip_table[num_ops+1, 'vertical'] == 'True':
					if self.pixel_strip_table[num_ops+1, 'flipped'] == '0':
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * - 1"
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass 
					elif self.pixel_strip_table[num_ops+1, 'flipped'] == '1':
						new_op.par.pay.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2"
						new_op.par.pax.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.pby.expr 		= "op('pixel_strip_table')[me.digits, 'length']/2 * -1"
						new_op.par.pbx.expr 		= "op('pixel_strip_table')[me.digits, 'pos']"

						new_op.par.points.expr 		= "op('pixel_strip_table')[me.digits, 'num_pixels']"
						pass
		pass 

	def Get_max_length(self):
		value_list = []
		if self.pixel_strip_table.numRows > 1:
			for i in range(1, self.pixel_strip_table.numRows):
				value_list.append(self.pixel_strip_table[i, 'length']) 

				max_length = max(value_list)
				pass 
		elif self.pixel_strip_table.numRows <=1:
			max_length = 0
			pass 
		return max_length

	def Get_max_height(self):
		value_list = []
		for i in range(1, self.pixel_strip_table.numRows):
			value_list.append(self.pixel_strip_table[i, 'pos']) 

			max_height = max(value_list)

			pass 
		return max_height

	def Delete_line_ops(self):
		num_ops = self.ownerComp.findChildren(type=lineSOP)

		for op in num_ops:
			op.destroy()
			pass 
		print('Deleted line ops in {}.'.format(self.ownerComp.name))
		print('- '*30)
		pass 

	def Clear_pixel_strip_table(self):
		self.pixel_strip_table.par.rows = 1
		print('Reset {}.'.format(self.pixel_strip_table.name))
		print('- '*30)
		pass 

#endregion

	def Add_pixel_module(self):
		pass 
