class CoursesController < ApplicationController
  def index
    #if there is a search query, properly handle rendering them
    if params[:q]
      @courses = Course.search(params[:q]).order("created_at DESC")
    else
      limit = 10
      @courses = Course.offset(params[:page].to_i * limit ).first(limit)
    end
    respond_to do |format|
      format.html
      format.json { render json: @courses }
    end
  end

  def show
    @course = Course.find(params[:id])
  end

  def new
    @course = Course.new()
  end

  def edit
    @course = Course.find(params[:id])
    #only those granted permission to edit a course should be able to edit them.
  end

  def viewing
    @course = Course.find(params[:id])
    @course_lesson = @course.course_lessons.find_by_position(params[:position])
    @lesson =  @course_lesson.lesson
    @lesson_version = @lesson.active_version
    render :template => 'lesson_versions/show'
  end

  def create
    @course = Course.new(course_params)
    respond_to do |format|
      if @course.save
        format.html { redirect_to @course, notice: 'Course was successfully created.' }
        format.json { render :show, status: :created, location: @course }
      else
        format.html { render :new }
        format.json { render json: @course.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    @course = Course.find(params[:id])
    respond_to do |format|
      if @course.update_attributes(course_params)
        format.html { redirect_to @course, notice: 'Course was successfully update.' }
        format.json { render :show, status: :updated, location: @course }
      else
        format.html { render :new }
        format.json { render json: @course.errors, status: :unprocessable_entity }
      end
    end
  end

  private
  def course_params
    params.require(:course).permit(:name, :description,
        :course_lessons_attributes => [:id, :_destroy, :position, :lesson_id])
  end

end
