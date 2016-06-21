class Track < ActiveRecord::Base
  default_scope { order('updated_at ASC') }
  has_many :track_courses
  has_many :courses, -> { distinct }, through: :track_courses
  has_many :topic_items, as: :topicable
  has_many :topics, -> { distinct }, through: :topic_items
  accepts_nested_attributes_for :track_courses, :reject_if => :all_blank, :allow_destroy => true
  accepts_nested_attributes_for :topic_items, :reject_if => :all_blank, :allow_destroy => true
  validates :name, presence: true

  def self.search(search)
    Track.where("name LIKE ? OR description LIKE ?", "%#{search}%", "%#{search}%").distinct
  end

  def as_json(options={})
    super(:only => [:id, :name, :description],
          :include => {
            :courses => {:only => [:id, :name, :description]}
          }
    )
  end
end
